# Optimal Code
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # number of rows and column
        m = len(mat)
        n = len(mat[0])
        # dictionary to map : (row + col) -> element on the diagonal
        mp = {}
        # store the final diagonal traversal
        result = []
        # group all matrix eleemnt by their diagonal index (row + col)
        for i in range(m):
            for j in range(n):
                # cells having the same values of (row + col) belong to the same diagonal
                key = i + j
                # create a new list for the diagonal if its does not exits
                if key not in mp:
                    mp[key] = []
                # store the current element
                mp[key].append(mat[i][j])
        # even diagonal are traversed upward odd diagonal downward
        flip = True
        # process diagonals in increasing order
        for key in sorted(mp.keys()):
            # reverse every alternate diagonal to obtain the required zigzg order
            if flip:
                mp[key].reverse()
            # add the current diagonal to the final answer
            result.extend(mp[key])
            # toggle the traversal direaction for the next diagonal
            flip = not flip
        # return the diagonal traversal
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)