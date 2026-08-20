// Brute Force Code & Optimal Code
class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        // base case: initial string contains only the character 'a'
        if (k == 1) {
            return 'a';
        }
        // total number of operations
        int n = operations.size();
        // current length of the string initially, the string contains only one character
        long long length = 1;
        // store the type of the operation that creates the k-th character
        int operation_type = 0;
        // store the corresponding position of the k-th character in the first half of the string
        long long new_k = 0;
        // find the first operation whose resulting string contains the k-th character
        for (int i = 0; i < n; i++) {
            // each operation doubles the string length
            length *= 2;
            // if the current string length is large enough the k-th character is created during this operation
            if (length >= k) {
                // save the operation type (0 or 1)
                operation_type = operations[i];
                // map the position in the second half back to the corresponding position in the first half
                new_k = k - (length / 2);
                // stop searching
                break;
            }
        }
        // recursively determine the original character before the current operation was applied
        char result = kthCharacter(new_k, operations);
        // if operation type is 0 the copied character remains unchanged
        if (operation_type == 0) {
            return result;
        }
        // if operation type is 1 increment the character by one. wrap around from 'z' to 'a'
        if (result == 'z') {
            return 'a';
        }
        // return the next alphabet character
        return result + 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)