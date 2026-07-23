# Brute Force Code
class Solution:
    # sort an array containing only 0, 1, 2 using bubble sort
    def sortColors(self, nums: List[int]) -> None:
        # total nunber of element
        n = len(nums)
        # perform bubble sort
        for i in range(n):
            # compare adjacent elements in each pass
            for j in range(n - 1):
                # swap the element if they are in wrong order
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # return the sorted array
        return nums 

# Time Complexity : O(N^2)
# Space Complexity : O(N)