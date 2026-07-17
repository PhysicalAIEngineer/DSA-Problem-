# Brute Force Code
class Solution:
    def __init__ (self):
        # total number of elements in the array
        self.n = 0
        # list to store all unique permutations
        self.result = []
    # backtracking functions to generate unique permutation using frequency map
    def backtrack(self, current: list[int], frequency: dict[int, int]):
        # if the current permutation contains all element store copy of its
        if len(current) == self.n:
            self.result.append(current[:])
            return 
        # try every distinct number avaliables 
        for number, count in frequency.items():
            # skip the number if all of its occurences have already been used
            if count == 0:
                continue
            # choose the current number
            current.append(number)
            frequency[number] -= 1
            # recur to bulid the remaining positions
            self.backtrack(current, frequency)
            # backtrack restoring the frequnecy and removing the numbers
            current.pop()
            frequency[number] += 1
    # return all unique permutations
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # storet the total number of elements
        self.n = len(nums)
        # clear any previous stored permutations
        self.result = []
        # dictionary to store the freuqency of each distinct numbers
        frequency = {}
        for number in nums:
            frequency[number] = (frequency.get(number, 0) + 1)
        # list to bulid the current permutations
        current = []
        # start generating unique permutaions
        self.backtrack(current, frequency)
        # return all permutations
        return self.result 

# Time Complexity : O(N!)
# Space Complexity : O(N)