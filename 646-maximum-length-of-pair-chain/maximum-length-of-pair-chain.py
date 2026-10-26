# Brute Force Code & Optimal Code
class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        # store the total number of pairs in the input list
        n = len(pairs)
        # sort the pairs in lexicographical orders
        pairs.sort()
        # create 2D memorization table with n rows and n column t[prev_index][curr_index] stores the maximum length of a chain can bulid by considering pairs starting at curr_index given that the previously slected pair is at prev_index and -1 mean that state has not been calculated yet, prev_index can also be -1 meaning no pairs has been selected
        t = [[-1] * n for _ in range(n)]
        # define a recursive helper function
        # - prev_index = index of the previously selected pair 
        # - curr_index = index of the currently being considered
        def lis(prev_index, curr_index):
            # base case : if curr_index reaches n all pairs have been considered there are no more pairs to add so return 0
            if curr_index == n:
                return 0
            # memoization check : if prev_index is valid and this state has already been calculated return the stored answer this avoid repeatedly solving the same subproblems
            if prev_index != -1 and t[prev_index][curr_index] != -1:
                return t[prev_index][curr_index]
            # option 1 : take the current pairs
            # intially assume that do not select the current pairs if the current pairs can be added to the chain update taken with the length obtained by selecting it
            take_current_pairs = 0
            # pair has from [start, end] can select the current pair if:
            # 1. prev_index == -1: no pair has been selected yet so the current pair can start the chain
            # 2. pairs[curr_index][0] > pairs[prev_index][1] : current pair start is strictly greater than previous pair end so the pairs from a valid chain
            if (prev_index == -1 or pairs[curr_index][0] > pairs[prev_index][1]):
                # select the current pairs
                # - add one because this pairs contributes one element to the chain update prev_index to curr_index because the current pair becomes the last pair selected in the chain continue considering pairs from curr_index + 1
                take_current_pairs = (1 + lis(curr_index, curr_index + 1))
            # option 2 : skip the current pairs
            # - do not include the current pair in the chain since did not select it prev_index remain unchanged move to the next pair and see the whethear longers chain can be formed without selecting the current pairs
            skip_current_pairs = lis(prev_index, curr_index + 1)
            # return the maximum chain length possible from this state
            result = max(take_current_pairs, skip_current_pairs)
            # store the result :  if prev_index is valid cache the larger of two choices
            # - take_current_pairs : chain length when selecting the current pair
            # - skip_current_pairs : chain length when selecting the current pairs
            # result can be reused if the same state is encounted
            if prev_index != -1:
                t[prev_index][curr_index] = result  
            return result
        # start from the first pairs with no previously selected pair prev_index = -1 means the first pairs in the chain be chosen from any pairs, provied the remaining pairs satisfy the chain condition
        return lis(-1, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)