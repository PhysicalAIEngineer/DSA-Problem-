# Brute Force Code & Optimal Code
class Solution: 
    def countCoveredBuildings(self, n, buildings): 
        # dictionary to store: y-coordinate -> [minimum x, maximum x] for every horizontal row (same y) find the leftmost and rightmost building.
        yToMinMaxX = {} 
        # dictionary to store: x-coordinate -> [minimum y, maximum y] for every vertical column (same x) find the bottommost and topmost building.
        xToMinMaxY = {} 
        # process every building
        for building in buildings: 
            # get the x and y coordinates
            x = building[0] 
            y = building[1] 
            # if this y-coordinate is seen for the first time initialize minimum x as infinity and maximum x as negative infinity
            if y not in yToMinMaxX: 
                yToMinMaxX[y] = [float('inf'), float('-inf')] 
            # if this x-coordinate is seen for the first time initialize minimum y as infinity and maximum y as negative infinity
            if x not in xToMinMaxY: 
                xToMinMaxY[x] = [float('inf'), float('-inf')] 
            # update the minimum x for this y-coordinate this gives the leftmost building in this row.
            yToMinMaxX[y][0] = min(yToMinMaxX[y][0], x) 
            # update the maximum x for this y-coordinate this gives the rightmost building in this row.
            yToMinMaxX[y][1] = max(yToMinMaxX[y][1], x) 
            # update the minimum y for this x-coordinate this gives the bottommost building in this column.
            xToMinMaxY[x][0] = min(xToMinMaxY[x][0], y) 
            # update the maximum y for this x-coordinate this gives the topmost building in this column.
            xToMinMaxY[x][1] = max(xToMinMaxY[x][1], y) 
        # stores the number of covered buildings
        result = 0 
        # check every building
        for building in buildings: 
            # get the x and y coordinates
            x = building[0] 
            y = building[1] 
            # get the minimum and maximum x for buildings having the same y
            xr = yToMinMaxX[y] 
            # get the minimum and maximum y for buildings having the same x
            yr = xToMinMaxY[x] 
            # building is covered if: building to its left xr[0] < x &  building to its right x < xr[1] & building below it  yr[0] < y &  building above it y < yr[1] all four conditions must be true.
            if (xr[0] < x < xr[1] and yr[0] < y < yr[1]): 
                # current building is covered
                result += 1 
        # return the total number of covered buildings
        return result

# Time Complexity : O(N)
# Space COmplexity : O(N)