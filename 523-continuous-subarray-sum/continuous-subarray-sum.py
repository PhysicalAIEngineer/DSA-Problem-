# Optimal Code
class Solution:
    # check if there exists continues subarray of length at least 2 whose sum is multiple of k
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # total number of elements
        n = len(nums)
        # dictionary to map : remainder -> first index where it appeared
        mp = {}
        # remainder of 0 is assumed to occur before the array starts this help handle subarrays that begin at index 0
        mp[0] = -1
        # running prefix sum
        prefix_sum = 0
        # traverse every elements
        for i in range(n):
            # update the prefix sum
            prefix_sum += nums[i]
            # compute the remaiders when dividing the prefix sum by k
            remainder = prefix_sum % k
            # if this remainder has alredy apprered before
            if remainder in mp:
                # subarray between the previous occurence and the current index has a sum divisible by k check that its length is at least 2
                if i - mp[remainder] >= 2:
                    return True
            else:
                # store only the first occurence of each remaiders because it gives the longest possible subarray
                mp[remainder] = i
        # no valid subarray found
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)