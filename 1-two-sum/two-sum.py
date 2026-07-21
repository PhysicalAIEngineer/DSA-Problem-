# Brute Force Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the total number of elements
        n = len(nums)
        # try every possible first element
        for i in range(n):
            # pair it with every element that comes after it
            for j in range(i + 1, n):
                # check whether the current pair adds up to the target
                if nums[i] + nums[j] == target:
                    # return the indices of the matching pairs
                    return [i, j]

# Time Complexity : O(N^2)
# Space Complexity : O(N)