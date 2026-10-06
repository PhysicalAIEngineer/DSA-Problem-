# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # store the expreesion
        self.s = ""
        # length of the expreesion
        self.n = 0
        # current index while parsing the expression
        self.idx = 0
    def getunit(self):
        # store all possible strings for the current unit
        result = set()
        # if current characters is "{" process everything inside the braces
        if self.s[self.idx] == "{":
            self.idx += 1
            # process the content inside {}
            result = self.performunion()
        else:
            # current characters is single alphabets
            result = {self.s[self.idx]}
        # move index to the next characters
        self.idx += 1
        return result
    def performConcat(self):
        # start with an empty string so that first unit can be concantenated
        result = {""}
        # continue while have characters of "{" because both can start new units
        while (self.idx < self.n and (self.s[self.idx] == "{" or self.s[self.idx].isalpha())):
            # get all possible strings for the current units
            temp = self.getunit()
            # store all possible concatenated strings
            concatresult = set()
            # combine every strings from result with every strings from temp
            for left in result:
                for right in temp:
                    concatresult.add(left + right)
            # update result with newly generated strings
            result = concatresult
        return result
    def performunion(self):
        # store all possible strings from union
        result = set()
        # continue until true
        while True:
            # process one concatenation parts
            temp = self.performConcat()
            # add all generated strings to result
            result.update(temp)
            # if "." is found move to the next union part
            if self.idx < self.n and self.s[self.idx] == ",":
                self.idx += 1
            else:
                # no more union parts
                break
        return result   
    def braceExpansionII(self, expression: str) -> list[str]:
        # stores expression and its length
        self.n = len(expression)
        self.s = expression
        # start parsing from index 0
        self.idx = 0
        # process the complete expression performunion the complete expreesion
        start = self.performunion()
        # so sort the final strings
        return sorted(start)

# Time Complexity : O(N)
# Space Complexity : O(N)