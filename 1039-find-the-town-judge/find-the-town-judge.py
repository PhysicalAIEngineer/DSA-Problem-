# Brute Force Code & Optimal Code
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # try every possible person as possible judge
        for person in range(1, n + 1):
            # count how many people trust the current person
            trusted_by = 0
            # track whether the current person trust someone
            trusts_someone = False
            # check every trust relationship
            for a, b in trust:
                # if the current person trust someone they cannot be the the judge
                if a == person:
                    trusts_someone = True
                # count how many people trust the current person
                if b == person:
                    trusted_by += 1
            # judge must : trust nobody & be trusted by every other person
            if (not trusts_someone and trusted_by == n - 1):
                return person
        # no judge exits
        return -1 

# Time Complexity : O(N^2)
# Space Complexity : O(N)