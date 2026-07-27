# Optimal Code
class Solution:
    # return the minimum number of arrows required to burst all balloons
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # total number of balloons
        n = len(points)
        # sort the balloons by their starting coordinate
        points.sort()
        # store the current overlapping interval of balloons
        prev = points[0]
        # at least one arrow is needed for the first group
        count = 1
        # traverse the remaining balloons
        for i in range(1, n):
            # current balloon interval
            curr_start = points[i][0]
            curr_end = points[i][1]
            # current overlapping interval
            prev_start = prev[0]
            prev_end = prev[1]
            # if there is no overlap a new arrow is required
            if curr_start > prev_end:
                count += 1
                # start a new overlapping interval
                prev = points[i]
            else:
                # overlap exists shrink the overlapping interval to the common intersection.
                prev[0] = max(prev_start, curr_start)
                prev[1] = min(prev_end, curr_end)
        # return the minimum number of arrows required
        return count

# Time Complexity : O(Nlong)
# Space Complexity : O(1)
