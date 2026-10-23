# Brute Force Code & Optimal Code
class Solution:
    def climbStairs(self, n: int) -> int:
        # create a memoization array of size 46 self.t[i] stores the number of ways to climb exactly i stairs initally every position contain -1 which mean that the answer of that number of stairs has not been calculated yet size 46 supports indices from 0 to 45
        self.t = [-1] * 46
        # define recursive helper function that return the number of distinct ways to reach stair n
        def solve(n):
            # base case : if there are 0 stairs there is 1 way to stay where are take no steps if there is 1 stair there is 1 way take one stap if there are 2 stairs there 2 ways : 1. take two 1 step moves & 2. take one 2 step move therefore the number of ways for n = 1 or n = 2 is n for n = 0 however the mathematically correct answer is 1
            if n == 0:
                return 1
            if n == 1 or n == 2:
                return n 
            # memoization check : if self.t[n] is not -1 have already calculted the number of ways to climb n stairs return the cached answer instend of recaculating it 
            if self.t[n] != -1:
                return self.t[n]
            # recursive case : to reach stair n the final move must be either : 1. one step move from stair n - 1 (number of ways to reach stair n - 1 : solve(n - 1)) 2. two step move from stair n - 2 (number of ways to reach stair n - 2: solve(n -2)) these possibilities are distinct so add their counts
            a = solve(n - 1)
            b = solve(n - 2)
            # store the calculated answer so that future calls to solve(n) can reuse it without repeating the work
            self.t[n] = a + b
            # return the total number of ways to climb n stairs
            return self.t[n]
        # begin the recursive calculation for the original number of stairs
        return solve(n)

# Time Complexity : O(N)
# Space Complexity : O(N) 
        