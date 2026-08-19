# Optimal Code
class Solution:
    # return the index with the minimum average diffrence
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # total number of elements
        n = len(nums)
        # calculate the total sum of all elements
        total_sum = sum(nums)
        # running sum of the left part
        left_sum = 0
        # running sum of the right part
        right_sum = 0
        # store the smallest average diffrence found so far
        min_diff = float("inf")
        # traverse every index as the split points
        for i in range(n):
            # include the current element in the left points
            left_sum += nums[i]
            # remaining elmeent belong to the right part
            right_sum = total_sum - left_sum
            # number of element in the left part
            left_count = i + 1
            # number of element in the right part
            right_count = n - left_count
            # compute the integer average of the left part
            left_avg = left_sum // left_count
            # compute the interger average of the right part if the right part is empy its average is defines as 0
            if i == n - 1:
                right_avg = 0
            else:
                right_avg = right_sum // right_count
            # compute the absolute diffrence between the two averages
            diff = abs(left_avg -  right_avg)
            # update the minimum diffrence and index
            if diff < min_diff:
                min_diff = diff
                result_index = i
        # return the index with the minimum average diffrence
        return result_index

# Time Complexity : O(N)
# Space Complexity : O(N) 