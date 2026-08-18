// Brute Force Code & Optimal Code
class Solution {
public:
    // count how many numbers exist between two consecutive prefixes: current and next_prefix in lexicographical order
    long long Count(long long current, long long next_prefix, long long n) {
        // store the total number of valid integers under the current prefix
        long long count_numbers = 0;
        // continue while the current prefix is within the range
        while (current <= n) {
            // count all numbers between the current prefix and the next prefix at this tree level
            count_numbers += min(next_prefix, n + 1) - current;
            // move one level deeper in the lexicographical tree
            current *= 10;
            next_prefix *= 10;
            // ensure the next prefix does not exceed n
            next_prefix = min(next_prefix, n + 1);
        }
        // return the number of integers under the current prefix
        return count_numbers;
    }
    // return the k-th smallest number in lexicographical order
    int findKthNumber(int n, int k) {
        // start from the smallest lexicographical number
        long long current = 1;
        // already standing at the first number so only k - 1 more moves are needed
        k--;
        // continue until the k-th number is reached
        while (k > 0) {
            // count how many numbers belong to the current prefix subtree
            long long count = Count(current, current + 1, n);
            // if the entire subtree can be skipped
            if (count <= k) {
                // move to the next sibling prefix
                current++;
                // skip all numbers in this subtree
                k -= count;
            }
            else {
                // otherwise move to the first child of the current prefix
                current *= 10;
                // one number the child itself is visited
                k--;
            }
        }
        // return the k-th lexicographical number
        return (int)current;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)