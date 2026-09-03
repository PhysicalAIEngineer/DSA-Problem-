# Brute Force Code & Optimal Code
class Solution:
    def countBadPairs(self, nums):
        # store the number of elements
        n = len(nums)
        # stores the total number of bad pairs
        result = 0
        # transform every element nums[i] = nums[i] - i this transformation helps us identify good pairs.
        for i in range(n):
            nums[i] = nums[i] - i
        # dictionary to store the frequency of each transformed value seen so far
        mp = {}
        # store the first transformed value because there are no previous elements for i = 0
        mp[nums[0]] = 1
        # process every element starting from index 1
        for j in range(1, n):
            # count how many previous elements have the same transformed value as nums[j] these elements form good pairs with j
            countOfNumsj = mp.get(nums[j], 0)
            # there are exactly j elements before index j because their indices are 0, 1, ..., j - 1
            totalNumsBeforej = j
            # previous elements with a different transformed value form bad pairs with index j
            badPairs = totalNumsBeforej - countOfNumsj
            # add the bad pairs found for this index
            result += badPairs
            # add the current transformed value to the frequency map
            mp[nums[j]] = mp.get(nums[j], 0) + 1
        # return the total number of bad pairs
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)