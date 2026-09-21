# Brute Force Code & Optimal Code
class Solution: 
    def numSubarraysWithSum(self, nums, goal): 
        # number of consecutive zeros before the first useful element
        prefix_zeros = 0 
        # sum of current sliding window
        window_sum = 0 
        # total number of subarrays having sum = goal
        count = 0 
        # left and right pointers
        i = 0 
        j = 0 
        # expand window using j
        while j < len(nums): 
            # add current element to window sum
            window_sum += nums[j] 
            # shrink window when nums[i] is 0, so we can remove it and create another valid subarray & window_sum becomes greater than goal
            while i < j and (nums[i] == 0 or window_sum > goal): 
                # If removing a 1, reset zero count
                if nums[i] == 1: 
                    prefix_zeros = 0 
                # if removing a 0, increase the number of extra starting positions
                else: 
                    prefix_zeros += 1 
                # remove nums[i] from current window
                window_sum -= nums[i] 
                # move left pointer forward
                i += 1 
            # if current window has the required sum count the current window plus all possible extra leading-zero choices
            if window_sum == goal: 
                count += 1 + prefix_zeros 
            # move right pointer forward
            j += 1 
        # return total number of valid subarrays
        return count

# Time Complexity : O(N)
# Space Complexity : O(N)  