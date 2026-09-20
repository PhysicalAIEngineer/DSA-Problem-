# Brute Force Code & Optimal Code
class Solution:
    def maxConsecutiveAnswers(self, answerkey: str, k: int) -> int:
        # variable to store the maximum valid window length
        result = k
        # dictionary to store the frequency of "T" and "F" in the current window
        frequency = {}
        # left pointer of the sliding window
        left = 0
        # traverse the string using the right pointer
        for right in range(len(answerkey)):
            # include the current characters in the sliding window
            current = answerkey[right]
            frequency[current] = (frequency.get(current, 0) + 1)
            # shrink the window while more than k flips are required
            while min(frequency.get("T", 0), frequency.get("F", 0)) > k:
                # remove the leftmost character from the current window
                frequency[answerkey[left]] -= 1
                # move the left pointer to shrink the window
                left += 1
            # update the maximum valid window length
            result = max(result, right - left + 1)
        # return the maximum number of consecutive equal answers
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)