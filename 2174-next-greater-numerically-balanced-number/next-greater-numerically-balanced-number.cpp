// Brute Force Code & Optimal Code
class Solution {
public:
    bool balanced(int num) {
        // create a frequency array for digits 0 to 9 freq[d] = how many times digit d appears
        vector<int> freq(10, 0);
        // extract every digit from the number
        while (num > 0) {
            // get the last digit
            int digit = num % 10;
            // increase the frequency of this digit
            freq[digit]++;
            // remove the last digit
            num /= 10;
        }
        // check the frequency of every digit
        for (int d = 0; d < 10; d++) {
            // if digit d appears in the number its frequency must be exactly d if the digit does not appear freq[d] = 0 which is allowed.
            if (freq[d] != 0 && freq[d] != d) {
                return false;
            }
        }
        // all digits satisfy the condition so the number is balanced
        return true;
    }
    int nextBeautifulNumber(int n) {
        // check every number starting from n + 1 because we need the next beautiful number
        for (int num = n + 1; num < 1224445; num++) {
            // check whether the current number is balanced
            if (balanced(num)) {
                // return the first balanced number found since check numbers in increasing order this is the smallest possible answer
                return num;
            }
        }
        // if no balanced number is found
        return -1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)