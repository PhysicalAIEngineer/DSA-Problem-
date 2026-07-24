# Brute Force Code & Optimal Code
class Solution:
    # find the maximum overlap between two binary images after translating one image in any direction
    def largestOverlap(self, img1, img2):
        # size of the square matrices
        n = len(img1)
        # store the maximum overlap found
        maximum_overlap = 0
        # try every possible vertical shift from -(n-1) to (n-1)
        for row_shift in range(-(n - 1), n):
            # try every possible horizontal shift from -(n-1) to (n-1)
            for col_shift in range(-(n - 1), n):
                # count the overlap for the current translation
                current_overlap = 0
                # traverse every cell in img1
                for i in range(n):
                    for j in range(n):
                        # compute the new position after applying the shift
                        new_row = i + row_shift
                        new_col = j + col_shift
                        # ensure the shifted position lies inside img2
                        if 0 <= new_row < n and 0 <= new_col < n:
                            # count the overlap if both images contain 1 at the corresponding cells
                            if img1[i][j] == 1 and img2[new_row][new_col] == 1:
                                current_overlap += 1
                # update the maximum overlap
                maximum_overlap = max(maximum_overlap, current_overlap)
        # return the largest overlap found
        return maximum_overlap

# Time Complexity : O(N^4)
# Space Complexity : O(N)