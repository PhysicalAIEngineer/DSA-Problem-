# Brute Force Code & Optimal Code
class Solution: 
    def solveQueries(self, nums, queries): 
        # store the length of the array
        n = len(nums) 
        # dictionary:
        # key   -> element
        # value -> list of all indices where that element occurs
        mp = {} 
        # store all positions of every element
        for i in range(n): 
            # if this element is not present in the dictionary create an empty list for it
            if nums[i] not in mp: 
                mp[nums[i]] = [] 
            # store the current index
            mp[nums[i]].append(i) 
        # store answers for all queries
        result = [] 
        # process every query
        for qi in queries:  
            # get the element present at the query index
            element = nums[qi] 
            # get all indices where this element occurs
            vec = mp[element] 
            # number of occurrences of this element
            sz = len(vec) 
            # if the element occurs only once there is no other occurrence to find
            if sz == 1: 
                result.append(-1) 
                continue 
            # find the position of qi inside vec using binary search (lower_bound)
            left = 0 
            right = sz - 1 
            while left <= right: 
                # find the middle position
                mid = (left + right) // 2 
                # if vec[mid] is smaller than qi search on the right side
                if vec[mid] < qi: 
                    left = mid + 1 
                # otherwise, search on the left side
                else: 
                    right = mid - 1 
            # left is the position of qi in vec
            pos = left 
            # start with the largest possible distance
            res = float('inf') 
            # check the right neighbour get the next occurrence after qi % sz handles the circular case: if pos is the last occurrence it goes back to the first occurrence
            right = vec[(pos + 1) % sz] 
            # normal absolute distance
            d = abs(qi - right) 
            # circular distance from index 8 to index 1 through the circular path = 10 - 7 = 3
            circularDist = n - d 
            # take the smaller of normal distance and circular distance
            res = min(res, d, circularDist) 
            # check the left neighbour get the previous occurrence before qi + sz and % sz handles the circular case when pos is 0
            left = vec[(pos - 1 + sz) % sz] 
            # normal absolute distance
            d = abs(qi - left) 
            # circular distance
            circularDist = n - d 
            # update the minimum distance
            res = min(res, d, circularDist) 
            # store the minimum distance for this query
            result.append(res) 
        # return answers for all queries
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)