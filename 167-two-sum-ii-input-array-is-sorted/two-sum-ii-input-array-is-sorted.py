# Optimal Code
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # intitalize two pointer:
        # - left starts at the beginning
        # - right starts at the end
        left = 0
        right = len(numbers) - 1
        # continue searching until the pointer meet
        while left < right:
            # calculate the sum of the current pairs
            current_sum = numbers[left] + numbers[right]
            # if the target sum is found return indices
            if current_sum == target:
                return [left + 1, right + 1]
            # if the current sum is greater than the target decrease the sum by moving the right pointer left
            if current_sum > target:
                right -= 1
            # otherwise increase the sum by moving the left pointer right
            else:
                left += 1
        # no valid pair found
        return []

# Time Complexity : O(N)
# Space Complexity : O(N)  