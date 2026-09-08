# Brute Force Code & Optimal Code
class Solution: 
    def numberOfSpecialChars(self, word): 
        # store the last position of each lowercase character
        # example: lastSmall[0] = last position of 'a'
        lastSmall = [-1] * 26 
        # store the first position of each uppercase character
        # example: firstCapital[0] = first position of 'A'
        firstCapital = [-1] * 26 
        # traverse every character in the word
        for i in range(len(word)): 
            # get the current character
            ch = word[i] 
            # if the character is lowercase
            if ch.islower(): 
                # store its latest index
                # ord(ch) - ord('a') converts:
                # 'a' -> 0
                # 'b' -> 1
                # ...
                # 'z' -> 25
                lastSmall[ord(ch) - ord('a')] = i 
            # otherwise, the character is uppercase
            else: 
                # store only the first occurrence of the uppercase character
                # example: if 'A' appears at index 3 store 3 and don't overwrite it later
                if firstCapital[ord(ch) - ord('A')] == -1: 
                    firstCapital[ord(ch) - ord('A')] = i 
        # store the number of special characters
        count = 0 
        # check all 26 letters
        for i in range(26):
            # character is special if:
            # 1. Its lowercase version exists
            # 2. Its uppercase version exists
            # 3. The last lowercase occurrence comes before the first uppercase occurrence
            # Example:
            # word = "aaAb"
            # lastSmall['a'] = 1
            # firstCapital['A'] = 2
            # 1 < 2, so 'a' is special
            if (lastSmall[i] != -1 and   firstCapital[i] != -1 and  lastSmall[i] < firstCapital[i]): 
                # found one special character
                count += 1 
        # return the total number of special characters
        return count

# Time Complexity : O(N)
# Space Complexity : O(N)