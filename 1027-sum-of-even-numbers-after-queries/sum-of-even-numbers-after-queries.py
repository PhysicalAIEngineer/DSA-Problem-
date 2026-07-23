# Optimal Code
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # calculate the initial sum of all even number 
        sum_even = 0
        for num in nums:
            if num % 2 == 0:
                sum_even += num
        # store the answer after each query
        result = []
        # process every query
        for val, idx in queries:
            # if the current element is even remove its contribution from the current even sum
            if nums[idx] % 2 == 0:
                sum_even -= nums[idx]
            # apply the updates
            nums[idx] += val
            # if the updated element is even, add its contribution back
            if nums[idx] % 2 == 0:
                sum_even += nums[idx]
            # store the current even sum
            result.append(sum_even)
        # return the even sums after all queires
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)