# Brute Force Code & Optimal Code
class Solution: 
    def resultsArray(self, nums, k): 
        # length of the array
        n = len(nums) 
        # there are (n - k + 1) windows of size k initially store -1 for every window
        result = [-1] * (n - k + 1) 
        # Count of consecutive increasing elements
        count = 1   
        # process the first window of size k
        for i in range(1, k): 
            # check if current element is exactly 1 greater than the previous element
            if nums[i] == nums[i - 1] + 1: 
                count += 1 
            else: 
                # consecutive sequence is broken start counting again from current element
                count = 1 
        # if all k elements are consecutive the last element is the answer
        if count == k: 
            result[0] = nums[k - 1] 
        # process remaining windows using sliding window
        i = 1 
        j = k 
        while j < n: 
            # check if nums[j] continues the consecutive sequence
            if nums[j] == nums[j - 1] + 1: 
                count += 1 
            else: 
                # sequence is broken start a new consecutive sequence
                count = 1 
            # if have at least k consecutive elements current window is valid
            if count >= k: 
                # largest element of the window is nums[j]
                result[i] = nums[j] 
            # move the sliding window forward
            i += 1 
            j += 1 
        # return the result for all windows
        return result

# Time Complexity : O(N)
# Spce Complexity : O(N)