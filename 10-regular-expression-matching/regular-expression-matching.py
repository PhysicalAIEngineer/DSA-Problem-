# Brute Force Code
class Solution:
    # recursive function to check whether the text matches the pattern
    def isMatch(self, text: str, pattern: str) -> bool:
        # base case: if the pattern is empty the text must also be empty for sucessful match
        if len(pattern) == 0:
            return len(text) == 0
        # check whether the first characters of the text matches the first characters of the pattern a "." in the pattern matches any single characters
        first_char_matched = (len(text) > 0 and (pattern[0] == text[0] or pattern[0] == "."))
        # if the second characters of the pattern "*" it means zero or more occurences of the precedding characters
        if len(pattern) >= 2 and pattern[1] == "*":
            return(
                # option 1: ignore the "x*" completely and move to the remaining pattern
                self.isMatch(text, pattern[2:]) or
                # option 2: if the first characters matches, consume one character from the text and contain using the same pattern becase "*" can match multiple characters
                (first_char_matched and self.isMatch(text[1:], pattern))
            )
        # if there is no "*" the first characters must watch then recursively match the remaining part of both the text and the pattern
        return (first_char_matched and self.isMatch(text[1:], pattern[1:]))

# Time Complexity : O(N)
# Space Complexity : O(N)