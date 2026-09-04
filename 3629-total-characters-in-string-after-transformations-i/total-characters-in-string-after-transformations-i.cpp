// Brute Force Code & Optimal Code
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        // modulo value to keep numbers within a manageable range
        long long M = 1000000007;
        // store the length of the original string
        int n = s.length();
        // frequency of each character index 0 = 'a', 1 = 'b', ..., 25 = 'z'
        vector<long long> mp(26, 0);
        // count how many times each character appears in s
        for (char ch : s) {
            mp[ch - 'a']++;
        }
        // perform the transformation t times
        for (int count = 1; count <= t; count++) {
            // temporary frequency array for the next transformation
            vector<long long> temp(26, 0);
            // process all 26 characters
            for (int i = 0; i < 26; i++) {
                // get the frequency of the current character
                long long freq = mp[i];
                // For characters 'a' to 'y'
                if (i != 25) {
                    // move the current frequency to the next character
                    temp[i + 1] = (temp[i + 1] + freq) % M;
                } else {
                    // add the frequency of z to both a and b
                    temp[0] = (temp[0] + freq) % M;
                    temp[1] = (temp[1] + freq) % M;
                }
            }
            // temporary array becomes the frequency array for the next transformation
            mp = temp;
        }
        // calculate the final length by adding frequencies of all 26 characters
        long long result = 0;
        for (int i = 0; i < 26; i++) {
            result = (result + mp[i]) % M;
        }
        // Return the final length after t transformations
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)