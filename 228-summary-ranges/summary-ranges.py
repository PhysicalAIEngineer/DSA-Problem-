# Optimal Code
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # number of element in the array
        n = len(nums)
        # if the array is empty there are not ranges to return
        if n == 0:
            return []
        # stroe the final list of ranges
        result = []
        # start processing from the first elements
        i = 0
        # continue until every element is processed
        while i < n:
            # store the first number of the current ranges
            start = nums[i]
            # keep moving forward while the numbers are consecutive
            while (i + 1 < n and nums[i] + 1 == nums[i + 1]):
                i += 1
            # if the starting and ending numbers are diffrent create range such 0 -> 2
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            # otherwise the range contains only one numbers
            else:
                result.append(str(start))
            # move the next unprocessed numbers
            i += 1
        # return all summarized ranges
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)