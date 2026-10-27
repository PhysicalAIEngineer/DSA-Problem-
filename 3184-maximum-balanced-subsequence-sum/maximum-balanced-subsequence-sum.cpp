// Brute Force Code & Optimal Code
#include <vector>
#include <algorithm>
#include <limits>
#include <set>
using namespace std;
class Solution {
public:
    long long maxBalancedSubsequenceSum(vector<int>& nums) {
        int n = nums.size();
        vector<long long> keys(n);
        for (int i = 0; i < n; ++i) {
            keys[i] = static_cast<long long>(nums[i]) - i;
        }
        set<long long> unique_keys(keys.begin(), keys.end());
        vector<long long> sorted_keys(unique_keys.begin(), unique_keys.end());
        int size = sorted_keys.size();
        vector<long long> bit(size + 1, 0);
        auto query = [&](int i) -> long long {
            long long best = 0;
            while (i > 0) {
                best = max(best, bit[i]);
                i -= i & -i;
            }
            return best;
        };
        auto update = [&](int i, long long value) -> void {
            while (i <= size) {
                bit[i] = max(bit[i], value);
                i += i & -i;
            }
        };
        long long answer = numeric_limits<long long>::min();
        for (int i = 0; i < n; ++i) {
            int rank = static_cast<int>(
                lower_bound(sorted_keys.begin(), sorted_keys.end(), keys[i]) - sorted_keys.begin()
            ) + 1;
            long long dp = static_cast<long long>(nums[i]) + query(rank);
            update(rank, dp);
            answer = max(answer, dp);
        }
        return answer;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)