# Brute Force Code & Optimal Code
class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        # variable to score the total number of fixed bound subarrays
        answer = 0
        # most recent index where minj was found
        minimum_position = -1
        # most recent index where maxk was found
        maximum_position = -1
        # most recent index of an element outside the valid range [mink, maxk]
        left_boundary = -1
        # traverse the array 
        for i in range(len(nums)):
            # if the current element is invalid update the left boundary 
            if nums[i] < mink or nums[i] > maxk:
                left_boundary = i
            # record the latest position of mink
            if nums[i] == mink:
                minimum_position = i
            # record the latest position of maxk
            if nums[i] == maxk:
                maximum_position = i
            # earliest of the latest position of mink and maxk determine how many valid subarray can end at index i 
            count = min(minimum_position, maximum_position) - left_boundary
            # only positive values contribute to the final answers
            answer += max(0, count)
        # return the total number of fixed bound subarray
        return answer 

# Time Complexity : O(N)
# Space Complexity : O(N)