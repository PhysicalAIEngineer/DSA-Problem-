# Brute Force Code & Optimal Code
class Solution:
    # return the total number of subarrays consisting only of zeros
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        # store the total number of zero-filled subarrays
        result = 0
        # count consecutive zeros ending at the current index
        count_subarrays = 0
        # traverse every element in the array
        for num in nums:
            # if the current element is zero extend the consecutive zero sequence
            if num == 0:
                count_subarrays += 1
            # otherwise, reset the consecutive zero count
            else:
                count_subarrays = 0
            # every consecutive zero ending at the current index forms a new zero-filled subarray
            result += count_subarrays
        # return the total number of zero-filled subarrays
        return result

# Time Complexity : O(N)
# Space Complexity : O(1)