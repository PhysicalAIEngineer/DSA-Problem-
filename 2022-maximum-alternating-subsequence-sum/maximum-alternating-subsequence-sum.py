# Brute Force Code & Optimal Code
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # store the total number of elements in nums
        n = len(nums)
        # create 2D memoization array with n rows and 2 columns t[index][iseven] stores the maximum alternating sum can obtain by considering element starting from index give the current sign state
        # 1. iseven = True -> next selected element gets a positive sign(+)
        # 2. iseven = False -> next selected element get a negative sign(-)
        # each entry start at -1 meaning that the state has not been calculated yet 
        maximum_alternating = [[-1] * 2 for _ in range(n)]
        # define recursive helper function solve(index, iseven) return the maximum altenating sum obtainable by considering nums[index:] with the given sign state
        def solve(index, iseven):
            # base case : if index is outside the array there are no element left to consider return 0 because no additional element can contribute to the alternating sum
            if index >= n:
                return 0
            # memoization check : use true as 1 and false as 0, so iseven can directly be used as column index in the memoization array if this state has already been calculated return its stored answer instend of solving it again
            if maximum_alternating[index][iseven] != -1:
                return maximum_alternating[index][iseven]
            # choice 1: skip the current element
            # do not include nums[index] in the subsequence since did not select an element the altenating sign state does not change move to the next index while keeping iseven unchanged
            skip_current_element = solve(index + 1, iseven)
            # choice 2: take the current element
            # start with value of the current element
            current_element = nums[index]
            # determine the sign of the current element 
            # 1. if iseven is true this is the next positive position value remain positive
            # 2. is iseven is false this is the next negative position negative value so that is subtracted from the sum
            if not iseven:
                current_element = -current_element
            # after selecting an element switch the sign state 
            # 1. if the current element was positive the next selected element must be negative 
            # 2. if the currnet element was negative the next selected element must be positive
            # add the current signed values to the best altenating sum obtainable from the remaining elements
            after_selecting_element = solve(index + 1, not iseven) + current_element
            # compare the two possibilities
            # 1. skip_current_element the current element 
            # 2. take the current element with its required sign
            # store the larger result in the memoization array
            maximum_alternating[index][iseven] = max(skip_current_element, after_selecting_element)
            # return the maximum altenating sum for this state
            return maximum_alternating[index][iseven]
        # start at index 0 with positive sign first selected element contributes positively subsequent selected elements altenative between negative and positive signs
        return solve(0, True)

# Time Complexity : O(N)
# Space Complexity : O(N) 