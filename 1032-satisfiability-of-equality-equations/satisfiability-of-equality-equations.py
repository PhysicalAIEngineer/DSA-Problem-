# Brute Forec Code & Optimal Code
class Solution:
    def find(self, i):
        # if i is not the root of its set recursively find the root
        if self.parent[i] != i:
            # path compression make i directly point to the root
            self.parent[i] = self.find(self.parent[i])
        # return the root 
        return self.parent[i]
    def union(self, x, y):
        # find the roots of x and y
        p_x = self.find(x)
        p_y = self.find(y)
        # if they belong to diffrent set merge to two sets
        if p_x != p_y:
            # union by rank attach the smaller rank tree under the larger rank tree
            if self.rank[p_x] > self.rank[p_y]:
                self.parent[p_y] = p_x
            elif self.rank[p_y] > self.rank[p_x]:
                self.parent[p_x] = p_y
            else:
                # both roots have the same rank attach p_x under p_y
                self.parent[p_x] = p_y
                # increase the rank of the new root
                self.rank[p_y] += 1
    def equationsPossible(self, equations: list[str]) -> bool:
        # there are 26 lowercase english letters
        self.parent = [0] * 26
        self.rank = [0] * 26
        # initally every character is in its own set
        for i in range(26):
            self.parent[i] = i
            self.rank[i] = 1
        # process all equality equations
        for s in equations:
            if s[1] == "=":
                # convert characters into numbers "a" -> 0 and "b" -> 1 then merge their sets
                self.union(ord(s[0]) - ord("a"), ord(s[3]) - ord("a"))
        # process all ineuality equations
        for s in equations:
            if s[1] == "!":
                # if both characters have the same root equality equations already connected them therfore this ineuality is impossible
                if self.find(ord(s[0]) - ord('a')) == self.find(ord(s[3]) - ord('a')): 
                    # connection found
                    return False
        # no return found 
        return True  