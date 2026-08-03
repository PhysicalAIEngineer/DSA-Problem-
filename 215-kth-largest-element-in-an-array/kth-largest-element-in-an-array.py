# Optimal Code
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create an empty min heap smallest element will always be available at index 0
        minheap = []
        # traverse every number in the array
        for num in nums:
            # add the current number in the array
            heapq.heappush(minheap, num)
            # if the heap contain more than k element remove the smallest element this ensures that the heap always contains only the k largest element seen so far
            if len(minheap) > k:
                heapq.heappop(minheap)
        # heap contain exactly k largest element smallest among these k elements is the kth largest element in the original array
        return minheap[0]

# Time Complexity : O(N)
# Space Complexity : O(N) 