# Optimal Code
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # number of element in the array
        n = len(nums)
        # calculate the total sum of all elements
        total_sum = 0
        # hash map to store : prefix_sum -> index where this prefix sum occurs 0 exists before the array start so its index is -1
        mp = {0: -1}
        # bulid the prefix sum map
        for i in range(n):
            # add the current element to the running sum
            total_sum += nums[i]
            # store the index of this prefix sum
            mp[total_sum] = i
        # if the total sum is smaller than x it is impossible to remove element whose sum is x
        if total_sum < x:
            return -1
        # instend of thinking about which element remove from the left and right think about which element should keep if total_sum = sum of removed element + sum of kept element and remove element must have sum x then sum of kept element = total_sum - x
        rest_sum = total_sum - x
        # store the maximum length of subarray whose sum is equal to rest_sum
        longest = float("-inf")
        # running prefix sum while searching for the longest valid subarray
        prefix_sum = 0
        # traverse the array
        for i in range(n):
            # add the curent element to the running prefix sum
            prefix_sum += nums[i]
            # subarray with sum = rest_sum if current_prefix - old_prefix = rest_sum then old_prefix = current_prefix - rest sum so this is the prefix sum need to find
            required = prefix_sum - rest_sum
            # if this required prefix sum existed before then the element between that index and i from subarray whose sum is rest_sum
            if required in mp:
                # calculate the length of this subarray
                current_length = i - mp[required]
                # keep the longest valid subarray
                longest = max(longest, current_length)
        # if no subarray with sum = rest_sum was found there is no valid way to remove element totaliing x 
        if longest == float("-inf"):
            return -1
        # keep the logest valid subarray everything outside this subarray must be removed so minimum operation = total element - kept element
        return n - longest

# Time Complexity : O(N)
# Space Complexity : O(N)