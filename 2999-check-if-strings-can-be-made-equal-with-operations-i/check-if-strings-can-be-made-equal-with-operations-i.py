# Brute Force Code & Optimal Code
class Solution: 
    def canBeEqual(self, s1, s2): 
        # check characters at index 0 and index 2 these two positions can be swapped with each other. so either: 1. both characters are already in the same positions or 2. The characters are swapped.
        condition1 = ( (s1[0] == s2[0] and s1[2] == s2[2])  or  (s1[0] == s2[2] and s1[2] == s2[0])) 
        # check characters at index 1 and index 3 these two positions can also be swapped with each other so either: 1. both characters are already in the same positions or 2. characters are swapped.
        condition2 = ( (s1[1] == s2[1] and s1[3] == s2[3])  or  (s1[1] == s2[3] and s1[3] == s2[1])) 
        # both independent conditions must be true so, 1. condition1 checks positions 0 and 2. and 2. condition2 checks positions 1 and 3 if both are true, s1 can be transformed into s2.
        return condition1 and condition2

# Time Complexity : O(N)
# Space Complexity : O(N)