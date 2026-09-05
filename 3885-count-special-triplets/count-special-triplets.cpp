// Brute Force Code & Optimal Code
class Solution {
private:
    int M;
public:
    Solution() {
        // modulo value to prevent the result from becoming too large
        M = 1e9 + 7;
    }
    int specialTriplets(const std::vector<int>& nums) {
        // stores how many times each number has appeared as a valid i
        std::unordered_map<int, int> valid_i;
        // stores how many valid (i, j) pairs are currently possible for each value of j
        std::unordered_map<int, int> valid_j;
        // stores the total number of valid triplets
        long long result = 0;
        // process each number as the current element which can act as k
        for (int num : nums) {
            // for a valid triplet, if num is k then k must be even because: nums[i] = nums[k] / 2 so the required j value is num / 2
            if (num % 2 == 0) {
                int target_j = num / 2;
                if (valid_j.find(target_j) != valid_j.end()) {
                    result = (result + valid_j[target_j]) % M;
                }
            }
            // check whether the current num can act as a valid j for a triplet: nums[i] = nums[j] * 2 therefore, we need previous i values equal to num * 2
            int required_i = num * 2;
            int count_i = 0;
            if (valid_i.find(required_i) != valid_i.end()) {
                count_i = valid_i[required_i];
            }
            if (valid_j.find(num) == valid_j.end()) {
                valid_j[num] = 0;
            }
            valid_j[num] = (valid_j[num] + count_i) % M;
            // current num can now act as i for future elements store its frequency
            if (valid_i.find(num) == valid_i.end()) {
                valid_i[num] = 0;
            }
            valid_i[num] += 1;
        }
        // return the total number of special triplets
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)