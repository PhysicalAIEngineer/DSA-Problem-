# Optimal Code
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # dictionary to store : number --> index
        mp = {}
        # traverse the array
        for i in range(len(nums)):
            # calculate the number needed to reach the target
            complement = target - nums[i]
            # if the complement has alredy been seen return its index and the current index
            if complement in mp:
                return [mp[complement], i]
            # store the current number along with its index
            mp[nums[i]] = i
        # no valid pair found
        return []

# Time Complexity : O(N)
# Space Complexity : O(N)