# Brute Force Code & Optimal Code 
class Solution: 
    def longestPalindrome(self, words): 
        # dictionary to store the frequency of words
        mp = {} 
        # stores the maximum length of the palindrome
        result = 0 
        # process every two-character word
        for word in words: 
            # reverse the current word
            reversedWord = word[::-1] 
            # Check if the reversed word is already available
            if mp.get(reversedWord, 0) > 0: 
                # one pair contains two words each word has 2 characters so, this pair adds 4 characters
                result += 4 
                # use one occurrence of the reversed word
                mp[reversedWord] -= 1 
            else: 
                # no matching reversed word is available yet store the current word in the dictionary
                mp[word] = mp.get(word, 0) + 1 
        # now check the remaining words that have the same two characters
        for word, count in mp.items(): 
            # Check whether both characters are the same
            if word[0] == word[1] and count > 0: 
                # one center word contains 2 character so, add 2 to the palindrome length
                result += 2 
                # only one equal-character word can be placed in the center
                break 
        # return the maximum length of the palindrome
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)