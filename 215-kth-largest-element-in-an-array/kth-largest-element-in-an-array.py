# Brute Force Code 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort the array in descending orders
        nums.sort(reverse = True)
        # indexing start from 0 the kth largest element is at index k - 1
        return nums[k - 1]

# Time Complexity : O(N)
# Space Complexity : O(N)