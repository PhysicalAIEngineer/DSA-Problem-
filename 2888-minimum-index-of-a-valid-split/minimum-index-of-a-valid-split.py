# Brute Force Code & Optimal Code
class Solution:
    def minimumIndex(self, nums):
        # store the total number of elements
        n = len(nums)
        # stores the frequency of elements in the left subarray
        mp1 = {}
        # stores the frequency of elements in the right subarray
        mp2 = {}
        # initially, all elements belong to the right subarray
        for num in nums:
            mp2[num] = mp2.get(num, 0) + 1
        # try every possible index as the partition point
        for i in range(n):
            # current element
            num = nums[i]
            # move the current element from the right subarray to the left subarray
            mp1[num] = mp1.get(num, 0) + 1
            mp2[num] -= 1
            # calculate the size of the left subarray left subarray = nums[0 ... i]
            n1 = i + 1
            # calculate the size of the right subarray right subarray = nums[i + 1 ... n-1]
            n2 = n - i - 1
            # check if 'num' is dominant in the left subarray and also dominant in the right subarray an element is dominant if: frequency * 2 > subarray size
            if mp1[num] * 2 > n1 and mp2[num] * 2 > n2:
                # found the smallest valid partition index
                return i
        # no valid partition index was found
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N)