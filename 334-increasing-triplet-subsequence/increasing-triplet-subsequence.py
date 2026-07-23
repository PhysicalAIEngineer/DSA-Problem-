# Optimal Code
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # store the smallest values first values of the triplet
        num1 = float("inf")
        # store the smallest possible second values of the triplet
        num2 = float("inf")
        # traverse every elements
        for num3 in nums:
            # if the current number is smaller than or equal to num1 update the smallest values
            if num3 <= num1:
                num1 = num3
            # otherwise if it is smaller than or equal to num2 update the second smallest values
            elif num3 <= num2:
                num2 = num3
            # if the current number is greater than both num1 and num2 then an increasing triplet exists num1 < num2 < num3
            else:
                return True
        # no incresing triplet was found
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)