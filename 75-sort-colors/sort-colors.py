# Optimal Code
class Solution:
    # sort an array contianing only 0, 1, 2, using counting
    def sortColors(self, nums: List[int]) -> None:
        # total number of elements
        n = len(nums)
        # count occurences of 0, 1, 2
        count_0 = 0
        count_1 = 0
        count_2 = 0
        # traverse the array and update the count
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1
        # overwrite the array in sorted array
        for i in range(n):
            # fill all 0 
            if count_0 > 0:
                nums[i] = 0
                count_0 -= 1
            # then fill all 1
            elif count_1 > 0:
                nums[i] = 1
                count_1 -= 1
            # finally fill all 2
            elif count_2 > 0:
                nums[i] = 2
                count_2 -= 1

# Time Complexity : O(N)
# Space Complexity : O(N)