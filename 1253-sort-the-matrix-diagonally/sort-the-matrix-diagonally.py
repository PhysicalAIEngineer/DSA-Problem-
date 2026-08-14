# Optimal Code
class Solution:
    # sort every diagonal of the matrix in ascending order                    
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # number of rows and columns
        m = len(mat)
        n = len(mat[0])
        # dicitonary to map : (row --> col) -> element of that diagonal
        mp = {}
        # collect all element of each diagonal
        for i in range(m):
            for j in range(n):
                # cells with the same values  of (row - columns) belong to the same diagonal
                key = i - j
                # crate the new list for this diagonal if it does not exists
                if key not in mp:
                    mp[key] = []
                # store the current element
                mp[key].append(mat[i][j])
        # sort the element of every diagonal
        for key in mp:
            mp[key].sort()
        # sorted values back into the matrix traverse from bottom right so that pop() removes the smallest remainning element from each sorted diagonal 
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                key = i - j
                mat[i][j] = mp[key].pop()
        # return the matrix with sorted diagonals
        return mat

# Time Complexity : O(Nlog)
# Space Complexity : O(N)