# Brute Force Code & Optimal Code 
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # answer can becomes extremely large because many different array mays satisfy the given condition to prevent the numbers from growing too large take every result modulo 10^9 + 7 as required by the problem
        mod = 10**9 + 7
        # no valid array can have more than n maximum discoveries
        if k > n or k == 0:
            return 0
        # create 3D memoization table t[index][search][maxsofar] stores the number of ways to fill the remaining position of the array
        # 1. index : index of the next position to fill
        # 2. searchcost : number of times new maximum has been found so far
        # 3. maxsofar : largest values encountered in the array so far
        # dimension are : 
        # 1. n + 1 : indices from 0 to n
        # 2. k + 2 : search costs from 0 to k + 1
        # 3. m + 1 : maximum values from 0 to m
        # initially every state contains -1 meaning it has no been calculated yet
        t = [[[-1] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        # define recursive helper function solve (index, searchcost, maxsofar) return the number of ways to complete the array so that the final search cost is exactly k given the current state of the array
        def solve(index, searchcost, maxsofar):
            # prune impossible states
            if searchcost > k:
                return 0
            # base case : if index == n all n position have been filled now check whether the total search cost is exactly k if it is this completed array is valid so return 1 to count this one way otherwise the array does not satisfy the requiremnt so return 0
            if index == n:
                return 1 if searchcost == k else 0
            # memoization check : check whether this exact state has already been solved state is determined by all three values : index, searchcost and maxsofar if a cached answer exists return it instend of recalculating all possible continuations
            if t[index][searchcost][maxsofar] != -1:
                return t[index][searchcost][maxsofar]
            # initalize the number of valid ways from this state will add the number of ways produced by choosing each possible values for the current array position
            number_valid = 0
            # try every possible values from 1 through m  from the current position array element must be between 1 to m 
            for i in range(1, m + 1):
                # case 1 : current values creates new maximum
                # if i is greaters than maxsofar this values is larger than every values encounterd earliers therefore the search algoritms would discover new maximum increasing searchcost by 1 new maximum becomes i move to the next index and count all valid ways to complete the array from this updated state
                if i > maxsofar:
                    number_valid += solve(index + 1, searchcost + 1, i)
                else:
                    # case 2 : current value does not create new maximum 
                    # if i <= maxsofar the current values is not larger than the maximum encounted so far
                    # therefore : searchcost does not change & maxsofar remains unchanged
                    # move to the next index and count all valid ways to complete the array from this state
                    number_valid += solve(index + 1, searchcost, maxsofar)
                number_valid %= mod
            # cache the result : after trying every possible value from 1 to m result contains the total number of valid completions from the current state modulo mod store it so that future calls to this same staete can reuse the answer
            t[index][searchcost][maxsofar] = number_valid
            return number_valid
        # start buliding the array from the first position
        # 1. index = 0 -> no position have been filled yet
        # 2. searchcost = 0 -> no new maximum has been discovered yet
        # 3. maxsofar = 0 -> intial maximum is 0 because all allowed values are positive integers from 1 to m
        # return the number of arrays of length n whose search cost is exactly k
        return solve(0, 0, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)