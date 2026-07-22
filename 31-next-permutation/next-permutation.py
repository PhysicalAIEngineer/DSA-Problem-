# Optimal Code
class Solution:
    # rearrange the array into its next lexicographical permutation
    def nextPermutation(self, nums):
        # total number of elements
        n = len(nums)
        # find the first index from the right where nums[i] > nums[i - 1] this identifies the pivot position
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        # if a pivot exists the current permutation is not the largest
        if i != 0:
            # store the index of the element to swap with the pivot
            index = i
            # find the smallest element greater than the pivot from the right side
            for j in range(n - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    index = j
                    break
            # swap the pivot with the selected element
            nums[i - 1], nums[index] = nums[index], nums[i - 1]
        # reverse the suffix starting from index i to obtain the smallest possible order
        left = i
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Time Complexity : O(N)
# Space Complexity : O(N)  
        