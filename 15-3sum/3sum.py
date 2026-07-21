# Optimal Code
class Solution:
    # find all pairs starting fromm index k whose sum equals the targets
    def twoSum(self, nums: list[int], k: int, result: list[list[int]], target: int):
        # intialize two pointer
        # - left start from index k
        # - right start from end
        left = k
        right = len(nums) - 1
        # continue until the pointer meet
        while left < right:
            # calculate the sum of the current pairs
            current_sum = nums[left] + nums[right]
            # if the sum is greater than the target, move the right pointer left
            if current_sum > target:
                right -= 1
            # if the sum is smaller than the target move the left pointer right
            elif current_sum < target:
                left += 1
            # valid pair is found
            else:
                # from the triplets using the fixed numbers
                result.append([-target, nums[left], nums[right]])
                # skip duplicate values on the left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # skip duplicate values on the right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # move both pointer to search for the next unique pairs
                left += 1
                right -= 1
    # return all unique triplets whose sum is equal to zero
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # at least three numbers are required
        if len(nums) < 3:
            return []
        # list to store all valid triplets
        result = []
        # sort the array so that two pointer can be applied
        nums.sort()
        # fix one number at a time
        for i in range(len(nums) - 2):
            # skip duplicates fixed elements to avoid duplicates triplets
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # find two number whose sum is equal to minus nums[i]
            self.twoSum(nums, i + 1, result, -nums[i])
        # return all unique triplets
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)