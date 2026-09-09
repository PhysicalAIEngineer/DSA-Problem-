// Brute Force Code & Optimal Code
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        // store the frequency of every number
        unordered_map<long long, int> mp;
        for (int num : nums) {
            // increase the frequency of the current number
            mp[num]++;
        }
        // store the maximum valid length found so far
        int result = 0;
        // special handling for number 1 if count of 1 is odd, we can use all of them
        if (mp[1] % 2) { // odd
            result = mp[1];
        }
        // if count of 1 is even use one less so that the remaining count is odd
        else { // even
            result = mp[1] - 1;
        }
        // try starting a valid sequence from every number
        for (auto& [num, freq] : mp) {
            // 1 is already handled separately
            if (num == 1) {
                continue;
            }
            // start the sequence with the current number
            long long curr = num;
            // store the length of the current sequence
            int length = 0;
            // at least two occurrences of curr are needed to form a pair: curr, curr then the next value becomes curr * curr
            while (mp.find(curr) != mp.end() && mp[curr] > 1) {
                // add two elements to the sequence
                length += 2;
                // move to the square of the current number
                curr = curr * curr;
            }
            // if the final value exists can add one more element
            if (mp.find(curr) != mp.end()) {
                length += 1;
            }
            // otherwise, the last pair cannot be completed properly, so remove those 2 elements
            else {
                length -= 1;
            }
            // update the maximum answer
            result = max(result, length);
        }
        // return the maximum valid length
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)