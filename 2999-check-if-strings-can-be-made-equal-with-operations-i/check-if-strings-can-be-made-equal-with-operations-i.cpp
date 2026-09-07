// Brute Force Code & Optimal Code
class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        // check characters at index 0 and index 2 these two positions can be swapped with each other so either: 1. both characters are already in the same positions or 2. the characters are swapped.
        bool condition1 = ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]));
        // check characters at index 1 and index 3 these two positions can also be swapped with each other so either: 1. both characters are already in the same positions or 2. characters are swapped.
        bool condition2 = ((s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]));
        // both independent conditions must be true
        // 1. condition1 checks positions 0 and 2
        // 2. condition2 checks positions 1 and 3
        // if both are true, s1 can be transformed into s2.
        return condition1 && condition2;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)