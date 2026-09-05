// Brute Force Code & Optimal Code
class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        // dictionary to store: y-coordinate -> [minimum x, maximum x] for every horizontal row (same y) find the leftmost and rightmost building.
        unordered_map<int, pair<int, int>> yToMinMaxX;
        // dictionary to store: x-coordinate -> [minimum y, maximum y] for every vertical column (same x) find the bottommost and topmost building.
        unordered_map<int, pair<int, int>> xToMinMaxY;
        // process every building
        for (auto& building : buildings) {
            // get the x and y coordinates
            int x = building[0];
            int y = building[1];
            // if this y-coordinate is seen for the first time initialize minimum x as infinity and maximum x as negative infinity
            if (yToMinMaxX.find(y) == yToMinMaxX.end()) {
                yToMinMaxX[y] = {INT_MAX, INT_MIN};
            }
            // if this x-coordinate is seen for the first time initialize minimum y as infinity and maximum y as negative infinity
            if (xToMinMaxY.find(x) == xToMinMaxY.end()) {
                xToMinMaxY[x] = {INT_MAX, INT_MIN};
            }
            // update the minimum x for this y-coordinate this gives the leftmost building in this row.
            yToMinMaxX[y].first = min(yToMinMaxX[y].first, x);
            // update the maximum x for this y-coordinate this gives the rightmost building in this row.
            yToMinMaxX[y].second = max(yToMinMaxX[y].second, x);
            // update the minimum y for this x-coordinate this gives the bottommost building in this column.
            xToMinMaxY[x].first = min(xToMinMaxY[x].first, y);
            // update the maximum y for this x-coordinate this gives the topmost building in this column.
            xToMinMaxY[x].second = max(xToMinMaxY[x].second, y);
        }
        // stores the number of covered buildings
        int result = 0;
        // check every building
        for (auto& building : buildings) {
            // get the x and y coordinates
            int x = building[0];
            int y = building[1];
            // get the minimum and maximum x for buildings having the same y
            pair<int, int> xr = yToMinMaxX[y];
            // get the minimum and maximum y for buildings having the same x
            pair<int, int> yr = xToMinMaxY[x];
            // building is covered if:
            // 1. building to its left  -> xr.first < x
            // 2. building to its right -> x < xr.second
            // 3. building below it     -> yr.first < y
            // 4. building above it     -> y < yr.second
            // all four conditions must be true.
            if (xr.first < x && x < xr.second && yr.first < y &&y < yr.second) {
                // current building is covered
                result++;
            }
        }
        // return the total number of covered buildings
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)