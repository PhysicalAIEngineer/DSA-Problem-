# Brute Force Code & Optimal Code
class Solution: 
    def helper(self, s, ch1, ch2): 
        # store the length of the string
        n = len(s) 
        # store the first index where each difference appears diff = count1 - count2
        diffMap = {} 
        # store the maximum balanced length found
        maxL = 0 
        # count occurrences of ch1 and ch2
        count1 = 0 
        count2 = 0 
        # traverse the string
        for i in range(n): 
            # if current character is neither ch1 nor ch2 the current substring is broken so start a new substring from the next position.
            if s[i] != ch1 and s[i] != ch2: 
                diffMap.clear() 
                count1 = 0 
                count2 = 0 
                continue 
            # count ch1
            if s[i] == ch1: 
                count1 += 1 
            # count ch2
            if s[i] == ch2: 
                count2 += 1 
            # if both characters have the same frequency the current substring is balanced.
            if count1 == count2: 
                maxL = max(maxL, count1 + count2) 
            # difference between the two character counts
            diff = count1 - count2 
            # if the same difference appeared before the substring between the previous index + 1 and current index has equal ch1 and ch2 counts.
            if diff in diffMap: 
                maxL = max(maxL, i - diffMap[diff]) 
            # store the first occurrence of this difference because it gives the longest possible substring.
            else: 
                diffMap[diff] = i 
        # return the longest balanced substring containing only ch1 and ch2
        return maxL 
    def longestBalanced(self, s): 
        # store the length of the string
        n = len(s) 
        # store the maximum balanced substring length
        maxL = 0 
        # case-1: Only one character 
        # count consecutive equal characters
        count = 1 
        for i in range(1, n): 
            # if current character is same as previous continue the current group.
            if s[i] == s[i - 1]: 
                count += 1 
            # otherwise, the current group ends.
            else: 
                maxL = max(maxL, count) 
                count = 1 
        # check the last group
        maxL = max(maxL, count) 
        # case-2: Two different characters 
        # find the longest balanced substring containing only 'a' and 'b'
        maxL = max(maxL, self.helper(s, 'a', 'b')) 
        # find the longest balanced substring containing only 'a' and 'c'
        maxL = max(maxL, self.helper(s, 'a', 'c')) 
        # find the longest balanced substring containing only 'b' and 'c'
        maxL = max(maxL, self.helper(s, 'b', 'c')) 
        # case-3: All three characters 
        # count occurrences of a, b and c
        countA = 0 
        countB = 0 
        countC = 0 
        # store the first index where each pair of differences appears.
        diffMap = {} 
        # traverse the string
        for i in range(n): 
            # count 'a'
            if s[i] == 'a': 
                countA += 1 
            # count 'b'
            if s[i] == 'b': 
                countB += 1 
            # count 'c'
            if s[i] == 'c': 
                countC += 1 
            # if a, b and c have the same frequency the substring from the beginning is balanced.
            if countA == countB and countA == countC: 
                maxL = max(maxL, countA + countB + countC) 
            # difference between number of a and b
            diffAB = countA - countB 
            # difference between number of a and c
            diffAC = countA - countC 
            # use both differences as one key same key at two positions means the substring between those positions has equal counts of a, b and c.
            key = (diffAB, diffAC) 
            # if this difference pair appeared before the substring between the previous position and current position is balanced.
            if key in diffMap: 
                maxL = max(maxL, i - diffMap[key]) 
            # otherwise, store the first occurrence.
            else: 
                diffMap[key] = i 
        # return the longest balanced substring length
        return maxL

# Time Complexity : O(N)
# Space Complexity : O(N)