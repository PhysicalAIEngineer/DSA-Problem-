# Optimal Code
class Solution:
    def minimumOperations(self, nums: list[int], target: list[int]) -> int:
        # number of elements in both arrays
        n = len(nums)
        # total number of operations required
        result = 0
        # difference required at the current index
        # 1. positive value -> need to increase nums[i]
        # 2. negative value -> need to decrease nums[i]
        curr = 0
        # difference required at the previous index use this to compare the current required change with the previous required change.
        prev = 0
        # traverse every position
        for i in range(n):
            # calculate how much nums[i] needs to change to become target[i].
            curr = target[i] - nums[i]
            # case 1: direction changes
            # previous position needed an increase but current position needs a decrease OR previous position needed a decrease but current position needs an increase. in either case, the previous subarray operation cannot continue into the current position.
            if (curr > 0 and prev < 0) or (curr < 0 and prev > 0):
                # need a completely new operation for the current required change.
                result += abs(curr)
            # case 2: Same direction
            # if current and previous requirements have the same direction, we may be able to reuse the operation from the previous position only need to pay for the additional amount that is greater than the previous requirement.
            elif abs(curr) > abs(prev):
                result += abs(curr - prev)
            # if abs(curr) <= abs(prev) no additional operation is needed here the operation already used for the previous position can cover the current requirement
            # current difference becomes the previous difference for the next iteration.
            prev = curr
        # return the minimum number of operations required
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)