# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the total number of words.
        self.n = 0
        # store the maximum score found so far initially, no valid selection has been processed, so use negative infinity.
        self.maxScore = float("-inf")
    def solve(self, i, score, words, currScore, freq):
        # update the maximum score every point during the recursion represents a valid selection of some words therefore, update the maximum score using the score obtained so far.
        self.maxScore = max(self.maxScore, currScore)
        # base case: if all words have been processed there are no more choices to make.
        if i >= self.n:
            return
        # try taking words[i] make a copy of the available letter frequencies modify this copy while checking whether the current word can be formed.
        tempFreq = freq.copy()
        # pointer used to process each character of the current word.
        j = 0
        # store the score of the current word.
        tempScore = 0
        # check whether words[i] can be formed
        while j < len(words[i]):
            # get the current character.
            ch = words[i][j]
            # convert the character into an index: 'a' -> 0, 'b' -> 1, 'z' -> 25
            index = ord(ch) - ord('a')
            # use one occurrence of this character.
            tempFreq[index] -= 1
            # add this character's score.
            tempScore += score[index]
            # if the frequency becomes negative do not have enough copies of this character.
            if tempFreq[index] < 0:
                break
            # move to the next character.
            j += 1
        # option 1: take words[i] if j reached the end of the word every required character was available.
        if j == len(words[i]):
            # continue processing the remaining words add the score of the current word to the current total score pass tempFreq because the letters used by this word are no longer available.
            self.solve(i + 1, score, words, currScore + tempScore,
                tempFreq)
        # do not take words[i] skip the current word and move to the next word use the original freq because the current word was not selected, so no letters were used.
        self.solve(i + 1, score, words, currScore, freq)
    def maxScoreWords(self, words: list[str], letters: list[str],score: list[int]) -> int:
        # create frequency array freq[i] stores how many copies of the character corresponding to index i are available.
        freq = [0] * 26
        # count the frequency of every available letter.
        for ch in letters:
            # convert character to an index.
            index = ord(ch) - ord('a')
            # increase its frequency.
            freq[index] += 1
        # reset the maximum score.
        self.maxScore = float("-inf")
        # store the number of words.
        self.n = len(words)
        # start backtracking from the first word.
        # initially:
        # - no words have been selected.
        # - current score is 0.
        # - all letters are available.
        self.solve(0, score, words, 0, freq)
        # return the maximum score found.
        return self.maxScore

# Time Complexity : O(N)
# Space Complexity : O(N)