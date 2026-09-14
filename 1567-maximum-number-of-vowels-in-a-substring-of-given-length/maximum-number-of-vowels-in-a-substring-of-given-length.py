# Brute Force Code & Optimal Code
class Solution:
    # check whether the given character is a lowercase vowel
    def isVowel(self, ch: str) -> bool:
        return (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')
    def maxVowels(self, s: str, k: int) -> int:
        # total number of characters in the string
        n = len(s)
        # variable to store the maximum number of vowels found in any window of size k
        maximum_vowels = 0
        # variable to store the number of vowels in the current window
        count = 0
        # sliding window pointers
        left = 0
        right = 0
        # traverse the string
        while right < n:
            # include the current character in the sliding window
            if self.isVowel(s[right]):
                count += 1
            # when the window size becomes exactly k
            if right - left + 1 == k:
                # update the maximum vowel count
                maximum_vowels = max(maximum_vowels,count)
                # remove the leftmost character from the current window
                if self.isVowel(s[left]):
                    count -= 1
                # shrink the window
                left += 1
            # expand the window
            right += 1
        # return the maximum number of vowels in any window
        return maximum_vowels

# Time Complexity : O(N)
# Space Complexity : O(N)