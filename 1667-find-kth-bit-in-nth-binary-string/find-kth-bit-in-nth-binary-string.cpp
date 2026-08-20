// Brute Force Code & Optimal Code
class Solution {
public:
    char findKthBit(int n, int k) {
        // base case: S1 = "0", so the only character is "0"
        if (n == 1) {
            return '0';
        }
        // calculate the length of the current string Sn formula: Sn = 2^n - 1
        int length = (1 << n) - 1;
        // find the middle position of Sn the middle character is always "1"
        int mid = (length + 1) / 2;
        // if the k-th position lies in the left half recursively search in S(n - 1)
        if (k < mid) {
            return findKthBit(n - 1, k);
        }
        // if k-th position is exactly the middle, return the fixed middle character
        else if (k == mid) {
            return '1';
        }
        // otherwise, the k-th position lies in the right half
        else {
            // find the mirrored position in the left half the right half is the reverse of S(n - 1)
            int mirrored_position = length - k + 1;
            // recursively find the bit at the mirrored position
            char ch = findKthBit(n - 1, mirrored_position);
            // right half is the inverted version so flip the returned bit
            if (ch == '0') {
                return '1';
            }
            else {
                return '0';
            }
        }
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)