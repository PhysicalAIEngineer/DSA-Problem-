# Brute Force Code
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # store each row : (number of soliders, row index)
        rows = []
        # traverse every row of the matrix
        for i in range(len(mat)):
            # count the number of soliders in the current row
            solider_count = 0
            # check every values in the current row
            for value in mat[i]:
                # "1" represents a soliders
                if value == 1:
                    solider_count += 1
            # store the solider count along with the original row index
            rows.append((solider_count, i))
        # sort the row weakest rows until will come first
        rows.sort()
        # store the indices of k weaksest rows
        result = []
        # take the first k rows after sorting
        for i in range(k):
            # rows[i][1] is original row index
            result.append(rows[i][1])
        # return the indices of the k weakest rows
        return result 

# Time Complexity : O(N^2)
# Space Compelxity : O(N)