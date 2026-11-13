# Brute Force Code & Optimal Code
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        # store the total number of element in the array
        n = len(nums)
        # if k is equal to n need to select every element since all element must be selected the origianl array itself is already the required subsequences return nums directly without performing any sorting
        if k == n:
            return nums
        # create an empty list to store each element along with its original index 
        vec = []
        # traverse the origianl array
        for i in range(n):
            # store the current element as tuples
            # 1. i = original index of the element
            # 2. nums[i] = actual values of the element
            vec.append((i, nums[i]))
        # sort the tuples in descedning order based on their values 
        vec.sort(key = lambda p: p[1], reverse = True)
        # select the first k tuples vec[:k] return the k element with the largest values then sort these selected tuples using their orginal indices 
        vec = sorted(vec[:k])
        # create an empty list to store the final subsequences
        result = []
        # traverse the k selected tuples
        for i in range(k):
            # each tuples has strutures : (original_index, values)
            # 1. vec[i][0] gives the original index
            # 2. vec[i][1] gives the actual element values
            # append only the values to the result
            result.append(vec[i][1])
        # return the selected k element in their original relative order 
        return result 

# Time Complexity : O(Nlog)
# Space Complexity : O(N) 
        