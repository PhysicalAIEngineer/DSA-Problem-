class Solution {
    int update(int op, int num, vector<int>& freq) {
        int res = 0;

        for (int i = 0; i < 32; i++) {
            if (num & 1)
                freq[i] += op;

            num >>= 1;

            if (freq[i])
                res |= (1 << i);
        }

        return res;
    }

public:
    int minimumDifference(vector<int>& nums, int k) {
        int l = 0, r = 0;
        int n = nums.size();

        vector<int> freq(32, 0);
        int ans = INT_MAX;

        while (r < n) {
            // Add nums[r]
            int orr = update(1, nums[r], freq);

            // Check current window
            ans = min(ans, abs(k - orr));

            // OR is already greater than k.
            // Removing elements can only decrease the OR.
            while (l < r && orr > k) {
                orr = update(-1, nums[l], freq);
                l++;

                ans = min(ans, abs(k - orr));
            }

            r++;
        }

        return ans;
    }
};