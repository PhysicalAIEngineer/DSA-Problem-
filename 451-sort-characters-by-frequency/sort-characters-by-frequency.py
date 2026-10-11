# Brute Force Code & Optimal Code
class Solution:
    def frequencySort(self, s: str) -> str:
        # create a list of (characters, frequency) pairs for ascii values 0 to 122
        vector = [("\0", 0)] * 123
        # count frequency of each characters
        for characters in s:
            # get the answer frequency of the characters
            frequency = vector[ord(characters)][1]
            # update the characters and increase its frequency by 1
            vector[ord(characters)] = (characters, frequency + 1)
        # sort characters by frequency in descending order
        vector.sort(key=lambda p: p[1], reverse=True)
        # store the final sorted string
        result = []
        # append each characters according to its frequency
        for i in range(123):
            characters, frequency = vector[i]
            result.append(characters * frequency)
        # return the string sorted by characters frequency
        return "".join(result)

# Time Complexity : O(Nlog)
# Space Complexity : O(N)