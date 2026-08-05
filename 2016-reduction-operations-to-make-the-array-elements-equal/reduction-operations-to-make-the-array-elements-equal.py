# Brute Force Code & Optimal Code
class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        # sort the array in ascending order after sorting, equal elements are grouped together and smaller values come before larger values.
        nums.sort()
        # store the total number of reduction operations
        count = 0
        # traverse the array from right to left start from the largest elements because larger values need to be reduced to smaller values.
        for i in range(len(nums) - 1, 0, -1):
            # if the current element is equal to the previous element, both belong to the same group of equal values do not need to add a new reduction level.
            if nums[i] == nums[i - 1]:
                continue
            # found a new distinct valueall elements from index i to the end are larger than nums[i - 1] number of elements in this group and all larger groups is: len(nums) - i each of these elements needs one operation to move down to the next smaller level.
            count += len(nums) - i
        # return the minimum number of operations
        return count

# Time Complexity : O(Nlog)
# Space Complexity : O(N)