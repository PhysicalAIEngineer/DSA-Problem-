# Brute Force Code & Optimal Code
class Solution: 
    def maxFrequency(self, nums, k): 
        # sort the array so we can increase smaller values up to the current largest value
        nums.sort() 
        # total number of elements
        n = len(nums) 
        # store maximum frequency found
        result = 0 
        # left pointer of sliding window
        i = 0 
        # sum of elements inside current window
        currSum = 0 
        # expand window using right pointer j
        for j in range(n): 
            # current largest value in the window
            target = nums[j] 
            # add current element to window sum
            currSum += nums[j] 
            # cost to make every element in the window equal to target required = (number of elements * target) - current sum
            if (j - i + 1) * target - currSum > k: 
                # window needs more than k operations so remove the leftmost element
                currSum -= nums[i] 
                i += 1 
            # update maximum valid window size
            result = max(result, j - i + 1) 
        # return maximum possible frequency
        return result

# Time Complexity : O(NlogN)
# Space Complexity : O(N)