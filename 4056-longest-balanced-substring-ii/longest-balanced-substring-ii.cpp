// Brute Force Code & Optimal Code
class Solution {
public:
    int helper(string& s, char ch1, char ch2) {
        // store the length of the string
        int n = s.length();
        // store the first index where each difference appears diff = count1 - count2
        unordered_map<int, int> diffMap;
        // store the maximum balanced length found
        int maxL = 0;
        // count occurrences of ch1 and ch2
        int count1 = 0;
        int count2 = 0;
        // traverse the string
        for (int i = 0; i < n; i++) {
            // if current character is neither ch1 nor ch2 the current substring is broken so start a new substring from the next position
            if (s[i] != ch1 && s[i] != ch2) {
                diffMap.clear();
                count1 = 0;
                count2 = 0;
                continue;
            }
            // count ch1
            if (s[i] == ch1) {
                count1++;
            }
            // count ch2
            if (s[i] == ch2) {
                count2++;
            }
            // if both characters have the same frequency the current substring is balanced
            if (count1 == count2) {
                maxL = max(maxL, count1 + count2);
            }
            // difference between the two character counts
            int diff = count1 - count2;
            // if the same difference appeared before the substring between the previous index + 1 and current index has equal ch1 and ch2 counts
            if (diffMap.find(diff) != diffMap.end()) {
                maxL = max(maxL, i - diffMap[diff]);
            }
            // store the first occurrence of this difference because it gives the longest possible substring
            else {
                diffMap[diff] = i;
            }
        }
        // return the longest balanced substring containing only ch1 and ch2
        return maxL;
    }
    int longestBalanced(string s) {
        // store the length of the string
        int n = s.length();
        // store the maximum balanced substring length
        int maxL = 0;
        // case-1: Only one character
        // count consecutive equal characters
        int count = 1;
        for (int i = 1; i < n; i++) {
            // if current character is same as previous continue the current group
            if (s[i] == s[i - 1]) {
                count++;
            }
            // otherwise, the current group ends
            else {
                maxL = max(maxL, count);
                count = 1;
            }
        }
        // check the last group
        maxL = max(maxL, count);
        // case-2: Two different characters
        // find the longest balanced substring containing only 'a' and 'b'
        maxL = max(maxL, helper(s, 'a', 'b'));
        // find the longest balanced substring containing only 'a' and 'c'
        maxL = max(maxL, helper(s, 'a', 'c'));
        // find the longest balanced substring containing only 'b' and 'c'
        maxL = max(maxL, helper(s, 'b', 'c'));
        // case-3: all three characters
        // count occurrences of a, b and c
        int countA = 0;
        int countB = 0;
        int countC = 0;
        // store the first index where each pair of differences appears
        map<pair<int, int>, int> diffMap;
        // traverse the string
        for (int i = 0; i < n; i++) {
            // count 'a'
            if (s[i] == 'a') {
                countA++;
            }
            // count 'b'
            if (s[i] == 'b') {
                countB++;
            }
            // count 'c'
            if (s[i] == 'c') {
                countC++;
            }
            // if a, b and c have the same frequency the substring from the beginning is balanced
            if (countA == countB && countA == countC) {
                maxL = max(maxL, countA + countB + countC);
            }
            // difference between number of a and b
            int diffAB = countA - countB;
            // difference between number of a and c
            int diffAC = countA - countC;
            // use both differences as one key same key at two positions means the substring between those positions has equal counts of a, b and c
            pair<int, int> key = {diffAB, diffAC};
            // if this difference pair appeared before the substring between the previous position and current position is balanced
            if (diffMap.find(key) != diffMap.end()) {
                maxL = max(maxL, i - diffMap[key]);
            }
            // otherwise, store the first occurrence
            else {
                diffMap[key] = i;
            }
        }
        // return the longest balanced substring length
        return maxL;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)