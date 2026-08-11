# Brute Force Code & Optimal Code
import math
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # dictionary to store the longest square streak
        mp = {}
        # sort the array in increasing order 
        nums.sort()
        # store the logest square streak found so far
        maxstreak = 0
        # process every number in sorted order
        for num in nums:
            # calculte the interger square root of num
            root = int(math.sqrt(num))
            # check whether num is perfect square
            if root * root == num and root in mp:
                # extend the square streak that ends
                mp[num] = mp[root] + 1
            else:
                # if num is not the square of previously processed number start new steak 
                mp[num] = 1
            # update the longest streak found so far
            maxstreak = max(maxstreak, mp[num])
        # valid square sterak must contain at least two numbers
        return -1 if maxstreak < 2 else maxstreak

# Time Complexity : O(Nlog)
# Space Complexity : O(N) 