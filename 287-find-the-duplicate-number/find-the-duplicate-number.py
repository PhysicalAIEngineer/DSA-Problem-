# Optimal Code
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # intialize both pointers at the first index array can be treated like list where nums[i] points to the next index
        slow = nums[0]
        fast = nums[0]
        # move slow pointer one step
        slow = nums[slow]
        # move fase pointer two step
        fast = nums[nums[fast]]
        # phase 1: find the point where slow and fast meet inside that cycle
        while slow != fast:
            # slow moves one step
            slow = nums[slow]
            # fast moves two step
            fast = nums[nums[fast]]
        # phase 2: reset slow to the starting point
        slow = nums[0]
        # move both pointer one step at a time they will meet at the start of the cycle which represents the duplicate number
        while slow != fast:
            # move slow one step
            slow = nums[slow]
            # move fast one step
            fast = nums[fast]
        # return meeting point is duplicates numbers
        return slow

# Time Complexity : O(N)
# Space Complexity : O(N)