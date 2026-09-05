# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # modulo value to prevent the result from becoming too large
        self.M = 10**9 + 7 
    def specialTriplets(self, nums): 
        # stores how many times each number has appeared as a valid i
        valid_i = {} 
        # stores how many valid (i, j) pairs are currently possible for each value of j
        valid_j = {} 
        # stores the total number of valid triplets
        result = 0 
        # process each number as the current element which can act as k
        for num in nums: 
            # for a valid triplet, if num is k then k must be even because: nums[i] = nums[k] / 2 so the required j value is num / 2
            if num % 2 == 0: 
                # add the number of valid (i, j) pairs where nums[j] = num / 2 these pairs can now form a triplet with the current num as k
                result = (result + valid_j.get(num // 2, 0)) % self.M 
            # check whether the current num can act as a valid j for a triplet: nums[i] = nums[j] * 2 therefore, we need previous i values equal to num * 2
            valid_j[num] = (valid_j.get(num, 0) + valid_i.get(num * 2, 0)) % self.M 
            # current num can now act as i for future elements store its frequency
            valid_i[num] = valid_i.get(num, 0) + 1 
        # return the total number of special triplets
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)