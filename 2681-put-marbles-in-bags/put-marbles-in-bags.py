# Optimal Code
class Solution:
    # return the difference between the maximum and minimum possible marble scores
    def putMarbles(self, weights: list[int], k: int) -> int:
        # number of marbles
        n = len(weights)
        # store the sum of every pair of adjacent weights
        # Example:
        # weights = [1, 3, 5, 1]
        # adjacent pair sums:
        # 1 + 3 = 4
        # 3 + 5 = 8
        # 5 + 1 = 6
        # pair_sum = [4, 8, 6]
        pair_sum = [0] * (n - 1)
        # calculate every adjacent pair sum
        for i in range(n - 1):
            pair_sum[i] = weights[i] + weights[i + 1]
        # sort the pair sums after sorting the smallest values are at the beginning and the largest values are at the end.
        pair_sum.sort()
        # store the minimum possible score
        min_sum = 0
        # store the maximum possible score
        max_sum = 0
        # if divide n marbles into k bags need exactly k - 1 cuts every cut between weights[i] and weights[i + 1] contributes weights[i] + weights[i + 1] therefore, only need to choose k - 1 adjacent pair sums.
        for i in range(k - 1):
            # for the minimum score choose the k - 1 smallest pair sums.
            min_sum += pair_sum[i]
            # for the maximum score choose the k - 1 largest pair sums n - i - 2 gives the index from the end.
            max_sum += pair_sum[n - i - 2]
        # first marble and the last marble appear in every possible partition score therefore, they cancel when calculating: maximum score - minimum score so only the selected cut pair sums matter.
        return max_sum - min_sum

# Time Complexity : O(N)
# Space Complexity : O(N)