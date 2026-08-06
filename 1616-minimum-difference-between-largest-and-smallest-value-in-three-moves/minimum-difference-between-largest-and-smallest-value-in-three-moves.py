# Brute Force Code & Optimal Code
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # number of elements in the array
        n = len(nums)
        # if the array has at most 4 elements can modify every element therefore all element can be made equal and the minimum diffrence becomes 0
        if n <= 4:
            return 0
        # sort the array so that the smallest and largest elements are easy to access
        nums.sort()
        # modify at most 3 element there are only four possible ways to do this:
        # 1. change the 3 largest elements
        # 2. change the 3 smallest elements
        # 3. change the 2 largest and 1 smallest elements
        # 4. change the 1 largest and 2 smallest elements
        # compute the remaining diffrence for each case and return the smallest ones
        return min(
            # case 1: modify the 3 largest element largest remaining element = nums[n - 4] and smallest remaining element = nums[0]
            nums[n - 4] - nums[0],
            # case 2: modify the 3 largest element largest remaining element = nums[n - 1] and smallest remaining element = nums[3]
            nums[n - 1] - nums[3],
            # case 3: modify the 2 largest element and 1 smallest element so, largest remaining element = nums[n - 3] and smallest remaining element = nums[1]
            nums[n - 3] - nums[1],
            # case 4: modify the 1 largest element and 2 smallest element so, largest remaining element = nums[n - 2] and smallest remaining element = nums[2]
            nums[n - 2] - nums[2]
        )

# Time Complexity : O(N)
# Space Complexity : O(1)