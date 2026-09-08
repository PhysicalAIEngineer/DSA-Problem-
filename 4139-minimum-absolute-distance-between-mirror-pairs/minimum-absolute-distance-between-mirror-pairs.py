# Brute Force Code & Optimal Code
class Solution:
    def getReverse(self, n: List[int]) -> int:
        # store the reversed numbers
        reversed = 0
        # cotinue until all digit are processed
        while n > 0:
            # get the last digit on n 
            rem = n % 10
            # add the digit to the reversed numbers
            reversed = reversed * 10 + rem
            # remove the last digit from n
            n //= 10
        # return the reversed numbers
        return reversed
    def minMirrorPairDistance(self, nums):
        # store the length of the array
        n = len(nums)
        # dictionary 
        # key --> reversed values
        # values --> index where that value was found
        mp = {}
        # store the minimum distance found so far
        result = float("inf")
        # traverse the array from left to right
        for i in range(n):
            # if nums[i] is already present in the map it means some previous number has reversed values equal to nums[i]
            if nums[i] in mp:
                # calculate the distance between the current index and previous index
                result = min(result, i - mp[nums[i]])
            # reverse the current number and store its index
            mp[self.getReverse(nums[i])] = i
        # if no mirror pair was found return -1 otherwise return the minimum distance
        return -1 if result == float("inf") else result 

# Time Complexity : O(N)
# Space Complexity : O(N)