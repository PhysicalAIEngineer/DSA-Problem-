# Brute Force Code
class Solution:
    # convert consecutive number into ranges and return them strings
    def summaryRanges(self, nums: list[int]):
        # stores the final list of ranges
        result = []
        # start processing from the first elements
        i = 0
        # continue until every number has been processed
        while i < len(nums):
            # store the first number of the current ranges
            start = nums[i]
            # store the last number of the current ranges
            last = nums[i]
            # start checking from the next elements
            j = i + 1
            # store the last consecutive number of the current ranges
            current = nums[i]
            # continue while there are more element to check
            while j < len(nums):
                # check whether the next number is consecutive with the current numbers
                if nums[j] == current + 1:
                    # extend the current ranges
                    current = nums[j]
                    # move the next element
                    j += 1
                # gap means the current ranges ends
                else:
                    break
            # if the range contains only one number store only that number
            if start == current:
                result.append(str(start))
            # if the range contains multiple consecutive number store it as start -> end
            else:
                result.append(str(start) + "->" + str(current))
            # continue from the first element that was not part of the current range
            i = j
        # return all summarized ranges
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N) 