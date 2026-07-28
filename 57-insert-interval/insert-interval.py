# Brute Force Code
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add the new interval to the existing list
        intervals.append(newInterval)
        # sort all intervals by their starting points
        intervals.sort()
        # store the final merged intervals
        result = []
        # traverse the every interval
        for interval in intervals:
            # if this is the first interval add its directly
            if len(result) == 0:
                result.append(interval)
            else:
                # get the last merged interval
                last_interval = result[-1]
                # check whether the current interval overlap with the last merged interval
                if interval[0] <= last_interval[1]:
                    # merge the intervals by extending the ending point
                    last_interval[1] = max(last_interval[1], interval[1]
                    )
                else:
                    # no overlap start new interval
                    result.append(interval)
        # return the merged interval
        return result 

# Time Complexity : O(Nlog)
# Space Complxity : O(1)