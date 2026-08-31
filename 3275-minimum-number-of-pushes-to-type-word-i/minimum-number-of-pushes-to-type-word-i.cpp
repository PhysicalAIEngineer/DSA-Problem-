// Brute Force Code & Optimal Code
class Solution {
public:
    int minimumPushes(string word) {
        // there are 8 keys available: 2, 3, 4, 5, 6, 7, 8, 9 if the word has 8 or fewer characters each character can be placed on a separate key therefore, every character needs only 1 push.
        if (word.length() <= 8) {
            return word.length();
        }
        // store the total number of pushes required.
        int count = 0;
        // store how many characters have been assigned to each key mp[key] = number of characters currently assigned to that key.
        unordered_map<int, int> mp;
        // start assigning characters from key 2.
        int assign = 2;
        // process every character in the word.
        for (char ch : word) {
            // there are only 8 keys: 2 through 9 after assigning a character to key 9 start again from key 2.
            if (assign > 9) {
                assign = 2;
            }
            // increase the number of characters assigned to the current key.
            mp[assign]++;
            // push count for a character depends on its position on the key:
            // 1st character -> 1 push
            // 2nd character -> 2 pushes
            // 3rd character -> 3 pushes
            // 4th character -> 4 pushes
            // mp[assign] gives the push count required for the current character.
            count += mp[assign];
            // move to the next key.
            assign++;
        }
        // return the total number of pushes.
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)