# Brute Force Code & Optimal Code
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # find the minimum and maximum elements
        minimum_elements = min(nums)
        maximum_elements = max(nums)
        # store the frequency of each number
        frequency = {}
        # count frequency of each numbers
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        # start filling the array from index 0
        i = 0
        # place numbers in sorted order from minimum and maximum using +1
        for num in range(minimum_elements, maximum_elements + 1):
            # repeat the number while its frequency is greater than 0
            while frequency.get(num, 0) > 0:
                nums[i] = num
                i += 1
                # decrease the frequency after placing the numbers
                frequency[num] -= 1
        # return the sorted array
        return nums

# Time Complexity : O(1)
# Space Complexity : O(1)
