# Optimal Code
import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # sort all intervals by their start times so sorting allow to process interval in the order in which they start
        intervals.sort()
        # create a min heap, this heap stores the end time of the interval currently occupying each group 
        min_heap = []
        # process every interval in increasing order of start times
        for interval in intervals:
            # start and end time of the current interval.
            start = interval[0]
            end = interval[1]
            # if the group whose interval ends earliest is free before this interval starts reuse that group '<' is important because intervals are closed: [1, 5] and [5, 10] overlap at 5.
            if min_heap and min_heap[0] < start:
                # remove the group whose interval ended earliest that group is now avalible and can be reused for the the current interval
                heapq.heappop(min_heap)
            # add the current interval end time to the heap this mean the current interval now occupies group until end 
            heapq.heappush(min_heap, end)
        # heap contain one end time for every currenlty required group therefore the number of element in the heap is the number of groups required
        return len(min_heap)

# Time Complexity : O(N)
# Space Complexity : O(N)