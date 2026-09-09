# Brute Force Code & Optimal Code
class Solution: 
    def maximumLength(self, nums): 
        # store the frequency of every number
        mp = {} 
        for num in nums: 
            # increase the frequency of the current number
            mp[num] = mp.get(num, 0) + 1 
        # store the maximum valid length found so far
        result = 0 
        # special handling for number 1 if count of 1 is odd, we can use all of them.
        if mp.get(1, 0) % 2:  # Odd 
            result = mp.get(1, 0) 
        # if count of 1 is even use one less so that the remaining count is odd
        else:  # Even 
            result = mp.get(1, 0) - 1 
        # try starting a valid sequence from every number
        for num in mp: 
            # 1 is already handled separately
            if num == 1: 
                continue 
            # start the sequence with the current number
            curr = num 
            # store the length of the current sequence
            length = 0 
            # least two occurrences of curr to form a pair: curr, curr then the next value becomes curr * curr
            while curr in mp and mp[curr] > 1: 
                # add two elements to the sequence
                length += 2 
                # move to the square of the current number
                curr = curr * curr 
            # if the final value exists can add one more element
            if curr in mp: 
                length += 1 
            # otherwise, the last pair cannot be completed properly, so remove those 2 elements
            else: 
                length -= 1 
            # update the maximum answer
            result = max(result, length) 
        # return the maximum valid length
        return result


# Time Complexity : O(N)
# Space Complexity : O(N)