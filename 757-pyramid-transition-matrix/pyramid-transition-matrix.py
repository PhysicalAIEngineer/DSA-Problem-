# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # memization dictionary stores whether particular state in possible or not
        self.t = {}
    def solve(self, current, mp, idx, above):
        # if only one characters is left the pyramid is succesfully formed
        if len(current) == 1:
            return True
        # create a unique key for the current states
        # current --> current row
        # idx --> current position
        # above --> row being contructed
        key = current + "_" + str(idx) + "_" + above
        # if this state was already calculated return the stored result
        if key in self.t:
            return self.t[key]
        # current row in completey processed move to the next row
        if idx == len(current) - 1:
            self.t[key] = self.solve(above, mp, 0, "")
            return self.t[key]
        # take two adjacent blocks from current row 
        # examples : current = "BCD", idx = 0 --> pairs = "BC"
        pair = current[idx:idx + 2]
        # if this pairs cannot produce any characters pyramid cannot be formed
        if pair not in mp:
            self.t[key] = False
            return False
        # try every possible characters that can be placed above this pairs
        for characters in mp[pair]:
            # do : add the selected characters to the next rows
            above += characters
            # explore : recursively continue buliding the current row
            if self.solve(current, mp, idx + 1, above):
                self.t[key] = True
                return True
            # undo : remove the last occurence and try another possibility
            above = above[:-1]
        # none of the possible characters worked
        self.t[key] = False
        return False
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # map each pairs to all possible characters that can be placed above its
        mp = {}
        # bulid mapping from allowed patterns 
        for pattern in allowed:
            pair = pattern[:2]
            characters = pattern[2]
            # create a list for this pairs if not parent
            if pair not in mp:
                mp[pair] = []
            # add possible characters for this pairs
            mp[pair].append(characters)
        # start buliding the pyramids from the bottom row idx = 0 and above = empty string
        return self.solve(bottom, mp, 0, "")

# Time Complexity : O(N)
# Space Complexity : O(N)