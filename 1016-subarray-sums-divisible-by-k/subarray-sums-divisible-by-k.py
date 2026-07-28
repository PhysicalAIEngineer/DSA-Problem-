# Optimal Code
class Solution:
    # return the number of subarrays whose sum is divisible by k
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # dictionary to store: remainder -> frequency
        remainder_frequency = {}
        # running prefix sum
        prefix_sum = 0
        # prefix sum with remainder 0 exists before the array starts
        remainder_frequency[0] = 1
        # store the total number of valid subarrays
        result = 0
        # traverse every element in the array
        for num in nums:
            # update the running prefix sum
            prefix_sum += num
            # compute the remainder when divided by k
            remainder = prefix_sum % k
            # Adjust negative remainders
            if remainder < 0:
                remainder += k
            # if this remainder has appeared before every previous occurrence forms a subarray whose sum is divisible by k
            if remainder in remainder_frequency:
                result += remainder_frequency[remainder]
            # record the current remainder
            remainder_frequency[remainder] = (remainder_frequency.get(remainder, 0) + 1)
        # return the total number of valid subarrays
        return result

# Time Complexity : O(N)
# Space Complexity : O(1)