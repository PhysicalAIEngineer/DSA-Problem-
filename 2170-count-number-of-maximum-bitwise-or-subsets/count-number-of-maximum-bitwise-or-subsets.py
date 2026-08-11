# Brute Force Code
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        # store the maximum bitwise or found so far. initially, no elements have been selected so the or value starts at 0.
        maximum_or = 0
        # store the number of subsets that have the maximum OR value found so far
        count = 0
        # generate all possible subsets using backtracking at every element, we have two choices: 1. include the current element and 2. do not include the current element this generates every possible subset.
        def backtrack(index, current_or, chosen):
            # need nonlocal because we want to update maximum_or and count inside this nested function.
            nonlocal maximum_or
            nonlocal count
            # Base case : if index reaches the length of nums have processed every element therefore, the current subset is complete.
            if index == len(nums):
                # ignore the empty subset chosen represents how many elements were included in the current subset.
                if chosen == 0:
                    return
                # found a new maximum OR if the OR of the current subset is greater than the maximum OR seen so far
                if current_or > maximum_or:
                    # update the maximum OR.
                    maximum_or = current_or
                    # since this is the new maximum all previous subsets are no longer considered maximum current subset is the first subset having this new maximum OR.
                    count = 1
                # found another subset with same maximum if the current subset has exactly the same OR as the maximum OR
                elif current_or == maximum_or:
                    # increase the number of subsets having the maximum OR.
                    count += 1
                # current subset has been processed.
                return
            # Choice 1: include nums[index]
            # add nums[index] to the current subset.
            # update the OR: current_or | nums[index]
            # also increase chosen because selected one more element.
            backtrack(index + 1, current_or | nums[index],chosen + 1)
            # Choice 2: Do not include nums[index]
            # leave current_or unchanged because nums[index] is not selected chosen also remains unchanged.
            backtrack(index + 1, current_or, chosen)
        # start generating subsets.
        # 1. index = 0  → start from the first element.
        # 2. current_or = 0 → no elements have been selected yet.
        # 3. chosen = 0 → The current subset is empty.
        backtrack(0, 0, 0)
        # return the number of non-empty subsets whose bitwise OR is equal to the maximum OR.
        return count

# Time Complexity : O(N!)
# Space Complexity : O(N)
        