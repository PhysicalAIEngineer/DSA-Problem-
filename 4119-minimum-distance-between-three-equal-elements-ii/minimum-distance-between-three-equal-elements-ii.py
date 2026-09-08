# Brute Force Code & Optimal Code
class Solution: 
    def minimumDistance(self, nums): 
        # store the length of the array
        n = len(nums) 
        # dictionary to store the indices of each number
        mp = {} 
        # store the minimum distance found start with infinity because have not found any valid triplet yet
        result = float('inf') 
        # traverse every index
        for k in range(n): 
            # if this number is appearing for the first time create an empty list to store its indices
            if nums[k] not in mp: 
                mp[nums[k]] = [] 
            # store the current index of this number
            mp[nums[k]].append(k) 
            # need at least 3 occurrences of the same number to form a valid triplet
            if len(mp[nums[k]]) >= 3: 
                # get all indices where the current number appeared
                vec = mp[nums[k]] 
                # number of occurrences of this number
                siz = len(vec) 
                # get the third-last occurrence
                i = vec[siz - 3] 
                # update the minimum distance between the first and third index
                result = min(result, k - i) 
        # If result is still infinity no number appeared at least 3 times
        if result >= float('inf'): 
            return -1 
        # required distance is 2 times the difference between the first and third index
        return 2 * result

# Time Complexity : O(N)
# Space Complexity : O(N)