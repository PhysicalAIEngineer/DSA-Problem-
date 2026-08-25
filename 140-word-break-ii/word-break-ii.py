# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store all valid sentences.
        self.result = []
        # store all dictionary words
        self.dict = set()
    def solve(self, i, currSentence, s):
        # if have reached the end of the string the current sentence is complete.
        if i >= len(s):
            self.result.append(currSentence)
            return
        # try every possible ending position for the current word.
        for j in range(i, len(s)):
            # create the substring from index i to j.
            tempWord = s[i:j + 1]

            # check whether the current substring exists in the dictionary.
            if tempWord in self.dict:
                # save the original sentence so can restore it after recursion.
                origSentence = currSentence
                # add a space if the sentence already contains a word.
                if currSentence:
                    currSentence += " "
                # add the current dictionary word.
                currSentence += tempWord
                # recursively process the remaining part of the string.
                self.solve(j + 1, currSentence, s)
                # backtrack restore the sentence to its previous state.
                currSentence = origSentence
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        # convert the word dictionary into a set for fast word lookup.
        for word in wordDict:
            self.dict.add(word)
        # current sentence.
        currSentence = ""
        # start backtracking from index 0.
        self.solve(0, currSentence, s)
        return self.result

# Time Complexity : O(N)
# Space COmplexity : O(N)