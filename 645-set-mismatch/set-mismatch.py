# Optimal Code
class Solution:
    # return the duplicated numbers and the missing number
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # total number of elements
        n = len(nums)
        # variable to store the missing and duplicates number
        missing = 0
        duplicates = 0
        # dictionary to map : number --> frequency
        mp = {}
        # count the frequency of every number in the array
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        # check every number from 1 to n 
        for i in range(1, n + 1):
            # if the number exists in the dictionary
            if i in mp:
                # frequency of 2 means the number is duplicated
                if mp[i] == 2:
                    duplicates = i
            else:
                # if the number is missing from the dictionary it is the missing numbers
                missing = i
        # return the duplicates and missing number
        return [duplicates, missing]

# Time Complexity : O(N)
# Space Complexity : O(1)