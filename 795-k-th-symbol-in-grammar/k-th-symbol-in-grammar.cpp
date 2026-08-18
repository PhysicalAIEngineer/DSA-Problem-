// Brute Force Code & Optimal Code
class Solution {
public:
    int kthGrammar(int n, int k) {
        // start with the assumption that the first symbol is always 0
        int current = 0;
        // define the range of possible positions in the nth row: [1, 2^(n-1)]
        long long left = 1;
        long long right = 1LL << (n - 1);
        // iterate n - 1 times
        for (int i = 0; i < n - 1; i++) {
            // midpoint splits the row into two halves
            long long mid = (left + right) / 2;
            // if k is in the left half symbol remains the same as the parent
            if (k <= mid) {
                right = mid;
            }
            else {
                // if k is in the right half symbol is flipped from the parent
                left = mid + 1;
                // flip between 0 and 1
                current = (current == 0) ? 1 : 0;
            }
        }
        // return the final symbol for row n, position k
        return current;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)