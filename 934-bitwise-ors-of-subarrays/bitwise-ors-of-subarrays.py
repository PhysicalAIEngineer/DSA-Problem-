# Brute Force Code & Optimal Code
class Solution: 
    def subarrayBitwiseORs(self, arr): 
        # stores all distinct or results of subarrays ending at the previous element
        prev = set() 
        # temporary set for or results of subarrays ending at the current element
        curr = set() 
        # stores all distinct or results found from every subarray
        result = set() 
        # process each number in the array
        for num in arr: 
            # take every or result from the previous position
            for x in prev: 
                # add the current number to the subarray and calculate its bitwise
                curr.add(x | num) 
                # store this or result globally
                result.add(x | num) 
            # start a new subarray containing only the current number
            curr.add(num) 
            # store the or result globally
            result.add(num) 
            # current or results become previous or results for the next iteration
            prev = curr 
            # clear curr so that it can be reused for the next number
            curr = set() 
        # return the number of distinct bitwise OR results
        return len(result)

# Time Complexity : O(N)
# Space Complexity : O(N)