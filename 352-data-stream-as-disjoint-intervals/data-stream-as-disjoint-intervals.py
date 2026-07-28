# Brute Force Code & Optimal Code
from sortedcontainers import SortedSet
class SummaryRanges:
    def __init__(self):
        # initalize a sorted set to store all unique numbers from the data stream
        self.st = SortedSet()
    # add number to the data stream
    def addNum(self, value: int) -> None:
        # insert the number into the sorted set
        self.st.add(value)
    # return the summary of disjoint intervals
    def getIntervals(self) -> List[List[int]]:
        # convert the sorted set into list for intervals
        nums = list(self.st)
        # store the resulting intervals
        result = []
        # total number of elements
        n = len(nums)
        # pointer to traverse the sorted numbers
        i = 0
        # process every numbers 
        while i < n:
            # start of the current intervals
            start = nums[i]
            # extend the intervals while consecutive numbers are found
            while (i < n - 1 and nums[i] + 1 == nums[i + 1]):
                i += 1
            # store the intervals as [start , end]
            result.append([start, nums[i]])
            # move to the next unprocessed numbers
            i += 1
        # return all disjoint intervals
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)
