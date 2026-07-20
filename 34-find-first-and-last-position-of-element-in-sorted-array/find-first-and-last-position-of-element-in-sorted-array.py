# Brute Force Code 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # store the first and last occurence of the target element
        first = -1
        last = -1
        # traverse the entire array
        for i in range(len(nums)):
            # check if the current eleement matches the target
            if nums[i] == target:
                # if this the first time the target is found store its index
                if first == -1:
                    first = i
                # update the last occurence every time the target is found
                last = i
        # return the indices of the first and last occurences if the target is not presents both values remain -1
        return [first, last]

# Time Complexity : O(N)
# Space Complexity : O(1)
        