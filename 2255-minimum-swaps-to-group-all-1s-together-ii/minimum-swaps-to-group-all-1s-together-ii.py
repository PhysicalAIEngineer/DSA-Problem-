# Brute Force Code & Optimal Code
class Solution: 
    def minSwaps(self, nums): 
        # length of the array
        n = len(nums) 
        # create a doubled array this helps us handle the circular nature of nums
        temp = [0] * (2 * n) 
        # copy nums twice
        for i in range(2 * n): 
            temp[i] = nums[i % n] 
        # total number of 1s in the array this will be the required window size
        countones = sum(nums) 
        # sliding window pointers
        i = 0 
        j = 0 
        # number of 1s in the current window
        currcount = 0 
        # maximum number of 1s found in any valid window
        maxcount = 0 
        # traverse the doubled array
        while j < 2 * n:
            # if current element is 1 add it to the current window count
            if temp[j] == 1: 
                currcount += 1 
            # window size should not be greater than the total number of 1s
            if j - i + 1 > countones:
                # remove the leftmost element from the current window
                currcount -= temp[i] 
                i += 1 
            # store the maximum number of 1s present in any window of size countOnes
            maxcount = max(maxcount, currcount)
            # move right pointer forward
            j += 1 
        # minimum swaps needed = total 1s - maximum 1s already present together
        return countones - maxcount

# Time Complexity : O(N)
# Space Complexity : O(N)