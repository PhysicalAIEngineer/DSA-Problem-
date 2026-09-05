# Brute Force Code & Optimal Code
class Solution:  
    def __init__(self): 
        # Modulo value to keep the result within a manageable range
        self.M = 10**9 + 7 
    def maximizeSquareArea(self, m, n, hFences, vFences): 
        # add the boundary fences horizontal boundaries are at 1 and m
        hFences.append(1) 
        hFences.append(m) 
        # add the boundary fences vertical boundaries are at 1 and n
        vFences.append(1) 
        vFences.append(n) 
        # sort the fence positions so can calculate distances between every pair
        hFences.sort() 
        vFences.sort() 
        # set to store all possible widths that can be created using vertical fences
        widths = set() 
        # set to store all possible heights that can be created using horizontal fences
        heights = set() 
        # generate all possible width by choosing every pair of vertical fences
        for i in range(len(vFences)): 
            for j in range(i + 1, len(vFences)): 
                # distance between two vertical fences gives a possible width
                width = vFences[j] - vFences[i] 
                # store this width set automatically removes duplicates
                widths.add(width) 
        # stores the largest side length that can be used for a square
        maxSide = 0 
        # generate all possible heights by choosing every pair of horizontal fences
        for i in range(len(hFences)): 
            for j in range(i + 1, len(hFences)): 
                # distance between two horizontal fences gives a possible height
                height = hFences[j] - hFences[i] 
                # if this height is also a possible width then can form a square
                if height in widths: 
                    # keep the largest possible side
                    maxSide = max(maxSide, height) 
        # if no common width and height were found it is impossible to make a square
        if maxSide == 0: 
            return -1 
        # area of square = side × side apply modulo to the final answer
        return (maxSide * maxSide) % self.M

# Time Complexity : O(N)
# Space Complexity : O(N)