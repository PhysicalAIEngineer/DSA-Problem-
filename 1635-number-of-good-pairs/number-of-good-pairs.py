# Brute Force Code & Optimal Code
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # dictionary to store the frequency of each number in the array
        mp = {}
        # count how many times each number appears
        for num in nums:
            # if num is already present increases its frequncy by 1 otherwise start its frequeny at 1.
            mp[num] = mp.get(num, 0) + 1
        # store the total number of good pairs
        result = 0
        # check every distinct numbers
        for num in mp:
            # get the number of times this values appears in the array
            count = mp[num]
            # if number appears count times choose any 2 occurence to form pair 
            result += (count * (count - 1) // 2)
        # return the total number of pairs where both indices contain the same values
        return result 

# Time Complexity : O(N)
# Space Complexity : O(1)