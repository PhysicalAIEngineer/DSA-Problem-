# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the final answer.
        self.result = ""
    def isSubsequence(self, s, sub, k):
        # pointer for traversing string s.
        i = 0
        # pointer for counting how many characters of sub * k have been matched.
        j = 0
        # length of the candidate subsequence.
        L = len(sub)
        # length of the original string.
        n = len(s)
        # check whether sub repeated k times can be formed as a subsequence of s.
        while i < n and j < k * L:
            # candidate string is repeated k times j % L gives the position inside sub.
            # Example:
            # sub = "abc"
            # j = 0 -> sub[0] -> 'a'
            # j = 1 -> sub[1] -> 'b'
            # j = 2 -> sub[2] -> 'c'
            # j = 3 -> sub[0] -> 'a'
            if s[i] == sub[j % L]:
                # current character matched.
                j += 1
            # move to the next character of s.
            i += 1
        # if matched all k copies of sub then sub repeated k times is a subsequence of s.
        return j == k * L
    def backtracking(self, s, curr, canUse, requiredFreq, k,maxLen):
        # if the candidate has reached the required length check whether it can be repeated k times as a subsequence of s.
        if len(curr) == maxLen:
            # check whether curr * k is a subsequence of s.
            if self.isSubsequence(s, curr, k):
                # store the valid candidate.
                self.result = curr
                # valid answer has been found.
                return True
            # candidate is not valid.
            return False
        # try characters from 'z' down to 'a' this is important because want the lexicographically largest answer.
        for i in range(25, -1, -1):
            # skip the character if:
            # 1. it does not appear at least k times.
            # 2. already used all allowed copies of this character.
            if not canUse[i] or requiredFreq[i] == 0:
                continue
            # convert the index back to a character.
            # 0  -> 'a'
            # 1  -> 'b'
            # ...
            # 25 -> 'z'
            ch = chr(i + ord('a'))
            # DO / CHOOSE
            # add the character to the current candidate.
            curr += ch
            # use one available copy of this character.
            requiredFreq[i] -= 1
            # -------------------------
            # EXPLORE
            # -------------------------
            # continue building the candidate string.
            if self.backtracking(s, curr, canUse, requiredFreq, k, maxLen):
                # valid answer was found.
                return True
            # UNDO / BACKTRACK
            # Remove the last chosen character.
            curr = curr[:-1]
            # Restore the available frequency.
            requiredFreq[i] += 1
        # no valid candidate could be created from this state.
        return False
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # length of the original string.
        n = len(s)
        # frequency of every character from 'a' to 'z'.
        freq = [0] * 26
        # count how many times each character appears in s.
        for ch in s:
            # convert character to an index: 'a' -> 0, 'b' -> 1, ..., 'z' -> 25.
            index = ord(ch) - ord('a')
            # increase the character frequency.
            freq[index] += 1
        # canUse[i] tells whether character i appears at least k times in s.
        canUse = [False] * 26
        # requiredFreq[i] tells the maximum number of times character i can appear in the answer.
        requiredFreq = [0] * 26
        # process every character.
        for i in range(26):
            # character must appear at least k times to appear once in a subsequence repeated k times.
            if freq[i] >= k:
                # this character can be used.
                canUse[i] = True
                # if a character appears freq[i] times it can appear at most freq[i] // k times in the candidate subsequence.
                # example:
                # - freq['a'] = 7, k = 3
                # - maximum number of 'a' in answer = 7 // 3 = 2
                requiredFreq[i] = freq[i] // k
        # answer repeated k times must fit inside s therefore, the maximum possible length of the candidate is n // k.
        maxLen = n // k
        # try candidate lengths from largest to smallest first valid length is automatically the maximum possible length.
        for length in range(maxLen, -1, -1):
            # backtracking modifies requiredFreq so create a fresh copy for each length.
            tempRequiredFreq = requiredFreq.copy()
            # start building a new candidate string.
            curr = ""
            # try to construct a valid candidate of the current length.
            if self.backtracking(s, curr, canUse, tempRequiredFreq, k, length):
                # because:
                # 1. try longer lengths first.
                # 2. try characters from 'z' to 'a'.
                # first valid answer is the longest and lexicographically largest one.
                return self.result
        # if no non-empty candidate was found return the empty string.
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)