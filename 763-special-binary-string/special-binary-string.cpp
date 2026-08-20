// Brute Force Code & Optimal Code
class Solution {
public:
    string makeLargestSpecial(string s) {
        // list to store all top-level special substrings
        vector<string> specials;
        // starting index of the current special substring
        int start = 0;
        // balance counter: '1' increases balance &  '0' decreases balance
        int balance = 0;
        // traverse the string to split it into top-level special substrings
        for (int i = 0; i < s.length(); i++) {
            // update the balance
            if (s[i] == '1') {
                balance++;
            } else {
                balance--;
            }
            // when balance becomes zero a complete special substring is found
            if (balance == 0) {
                // extract the inner portion by removing the outermost '1' and '0'
                string inner = s.substr(start + 1, i - start - 1);
                // recursively rearrange the inner substring to make it lexicographically largest
                string largestInner = makeLargestSpecial(inner);
                // rebuild the special substring
                string special = "1" + largestInner + "0";
                // store the special substring
                specials.push_back(special);
                // start searching for the next top-level special substring
                start = i + 1;
            }
        }
        // arrange all top-level special substrings in descending lexicographical order
        sort(specials.rbegin(), specials.rend());
        // build the final largest special string
        string result = "";
        for (string current : specials) {
            result += current;
        }
        // return the lexicographically largest special binary string
        return result;
    }
};

// Time Complexity : O(N^2logN)
// Space Complexity : O(N)