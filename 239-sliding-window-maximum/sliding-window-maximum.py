# Brute Force Code & Optimal Code
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max heap implemented using negative values
        max_heap = []
        # list to store the maximum element of each sliding window
        result = []
        # total number of element in the array
        n = len(nums)
        # traverse the array
        for i in range(n):
            # remove element from the heap that are no longers inside the current sliding windows 
            while (max_heap and max_heap[0][1] <= i - k):
                heapq.heappop(max_heap)
            # insert the current element along with its index into the max heap
            heapq.heappush(max_heap, (-nums[i], i))
            # once the first window of size k is formed the heap top element is the maximum values
            if i >= k - 1:
                result.append(-max_heap[0][0])
        # return the maximum values for every sliding winodw
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)