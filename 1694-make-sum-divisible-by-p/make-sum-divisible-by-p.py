# Brute Force Code & Optimal Code
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # number of element in the array
        n = len(nums)
        # calculate the total sum of the array modulo p
        sum = 0
        # calculate total sum % p
        for num in nums:
            sum = (sum + num) % p
        # remove a subarray whose sum % p is equal to the remainder of the total sum
        target = sum % p
        # dictionary to store : prefix_sum_remainder -> latest index
        mp = {}
        # if the total sum is alredy divisible by p no subarray needs to tbe removed
        if target == 0:
            return 0 
        # before the array starts the prefix sum is 0 , index = -1 represents the position before the first element this help us handle subarray that start from index 0
        mp[0] = -1
        # store the current prefix sum modulo p
        current = 0
        # store the minimum length of valid subarray found so far intially use n because n is the maximum possible subarray length
        result = n
        # traverse the array from left to right
        for j in range(n):
            # update the prefix sum modulo p, current represents : (nums[0] + nums[1] + ..........+ nums[j]) % p
            current = (current + nums[j]) % p
            # suppose : previous prefix remainder = previous and current prefix remainder = current so the sum of subarray between previous index and j is (current - previous) % p threfore : (current - previous) % p = target
            remainder = (current - target + p) % p
            # check the whether have already seen this required prefix remainder
            if remainder in mp:
                # if remainder was previously found at index: mp[remainder] than the subarray from mp[remainder] + 1 to j has sum % p == target its length is j - mp[remainder] keep the shortest valid subarray
                result = min(result, j - mp[remainder])
            # store the current prefix remainder with the current index store the lastest index so that when the same remainder appears again the shoretest possible subarray
            mp[current] = j
        # if result is still n never found a valid subarray in that case return -1 otherwise return the minimum length found
        return -1 if result == n else result 

# Time Complexity : O(N)
# Space Complexity : O(N)