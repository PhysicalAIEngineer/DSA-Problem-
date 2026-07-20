# Brute Force Code
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # assume the first element is the minimum values
        minimum = nums[0]
        # traverse the entire array
        for i in range(len(nums)):
            # if the current element is smallers than the stored minimum update the minimum values
            if nums[i] < minimum:
                minimum = nums[i]
        # return the smallest element in the array
        return minimum 

# Time Complexity : O(N)
# Space Complexity : O(1)
        