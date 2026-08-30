// Brute Force Code & Optimal Code
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        // modulo value used because the answer can become very large.
        const int MOD = 1e9 + 7;
        // number of elements in the array.
        int n = arr.size();
        // sort the array this allows us to process smaller values before larger values.
        sort(arr.begin(), arr.end());
        // dp[x] = number of different binary trees that can be formed with x as the root.
        unordered_map<int, long long> mp;
        // single element by itself forms one valid binary tree.
        mp[arr[0]] = 1;
        // process every value starting from the second element.
        for (int i = 1; i < n; i++) {
            // at minimum, arr[i] can form a single-node tree.
            long long count = 1;
            // try every previously processed value as the left child.
            for (int j = 0; j < i; j++) {
                // choose arr[j] as the left child.
                int left = arr[j];
                // for arr[i] to be the root: left * right = arr[i] therefore: right = arr[i] / left check that arr[i] is divisible by left and that the right child exists.
                if (arr[i] % left == 0 &&
                    mp.find(arr[i] / left) != mp.end()) {
                    // number of ways to build the left subtree.
                    long long leftWays = mp[left];
                    // number of ways to build the right subtree.
                    long long rightWays = mp[arr[i] / left];
                    // every left subtree can be combined with every right subtree. total combinations = leftWays * rightWays
                    count += leftWays * rightWays;
                    // apply modulo to keep the value small.
                    count %= MOD;
                }
            }
            // store the number of binary trees having arr[i] as the root.
            mp[arr[i]] = count;
        }
        // store the total number of valid trees.
        long long result = 0;
        // add the number of trees for every possible root value.
        for (auto& it : mp) {
            // apply modulo to keep the number small.
            result = (result + it.second) % MOD;
        }
        // return the total number of factored binary trees.
        return result;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)