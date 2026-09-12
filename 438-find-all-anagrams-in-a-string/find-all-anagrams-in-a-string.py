# Brute Force Code & Optimal Code
class Solution:
  def findAnagrams(self, s: str, p: str):
    # frequency array to store the characters counts of the pattern
    count = [0] * 26
    # length of the text and the pattern
    m = len(s)
    n = len(p)
    # store the frequency of each character in the pattern
    for ch in p:
      count[ord(ch) - ord('a')] += 1
    # initalize the sliding window pointer
    left = 0
    right = 0
    # list to store the starting indices of all anagrams
    result = []
    # traverse the text using a sliding windows
    while right < m:
      # include the current characters in the window by decreasing its required frequency
      count[ord(s[right]) - ord('a')] -= 1
      # when the window size becomes equal to the pattern length
      if right - left + 1 == n:
        # if all frequencies are zero the current window is an anagram of the pattern
        if count == [0] * 26:
          result.append(left)
        # remove the leftmost characters from the window before sliding window forward
        count[ord(s[left]) - ord('a')] += 1
        left += 1
      # expand the window
      right += 1
    # return the list of starting indices
    return result

# Time Complexity : O(N)
# Space Complexity : O(1)