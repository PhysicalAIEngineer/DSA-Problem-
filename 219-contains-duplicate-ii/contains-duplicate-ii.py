# Brute Force Code & Optimal Code
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        # total number of elements in the array
        n = len(nums)
        # set to store the elements currently inside the sliding window 
        seen = set()
        # intialize the sliding window pointer
        left = 0
        right = 0
        # traverse the array using the right pointer
        while right < n:
            # if the window size becomes greater than k remove the leftmost element from the window
            if abs(left - right) > k:
                seen.remove(nums[left])
                left += 1
            # if the current element already exists in the window nearby duplicate has been found
            if nums[right] in seen:
                return True
            # add the current element to the sliding window
            seen.add(nums[right])
            # expand the window by moving the right pointer
            right += 1
        # no nearby duplicate exisits
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)
        