# Brute Force Code & Optimal Code
class Solution: 
    def countSubarrays(self, nums, k): 
        # find the maximum element in the array
        maxE = max(nums) 
        # length of the array
        n = len(nums) 
        # left and right pointers of sliding window
        i = 0 
        j = 0 
        # total number of valid subarrays
        result = 0
        # count of maximum elements in current window
        countMax = 0 
        # expand window using j
        while j < n: 
            # if current element is the maximum increase its count
            if nums[j] == maxE: 
                countMax += 1 
            # if window contains at least k maximum elements
            while countMax >= k: 
                # every index from j to n-1 can be the ending point of a valid subarray
                result += n - j 
                # if nums[i] is maximum remove it from the window
                if nums[i] == maxE: 
                    countMax -= 1 
                # move left pointer forward
                i += 1 
            # move right pointer forward
            j += 1 
        # return total number of valid subarrays
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)