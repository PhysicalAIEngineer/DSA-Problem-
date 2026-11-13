// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        // store the total number of elements in the array.
        int n = nums.size();
        // if k is equal to n, we need to select every element since all elements must be selected, the original array itself is already the required subsequence.
        // return nums directly without performing any sorting.
        if (k == n) {
            return nums;
        }
        // create a vector to store each element along with its original index.
        // each pair contains:
        // 1. first  -> original index of the element.
        // 2. second -> actual value of the element.
        vector<pair<int, int>> vec;
        // traverse the original array.
        for (int i = 0; i < n; i++) {
            // store the current element as a pair.
            // first  = original index.
            // second = nums[i], the actual element value.
            vec.push_back({i, nums[i]});
        }
        // sort the pairs in descending order based on their element values lambda function compares the second element of each pair. if p1.second is greater than p2.second p1 comes before p2.
        sort(vec.begin(), vec.end(),
             [](const pair<int, int>& p1,
                const pair<int, int>& p2) {
                    return p1.second > p2.second;
             });
        // select the first k pairs these k pairs contain the k largest values then sort the selected pairs using their original indices so that the selected elements appear in their original relative order.
        vec.resize(k);
        // sort the selected pairs in ascending order based on their original indices.
        sort(vec.begin(), vec.end());
        // create an empty vector to store the final subsequence.
        vector<int> result;
        // traverse the k selected pairs.
        for (int i = 0; i < k; i++) {
            // each pair has the following structure:
            // vec[i].first  -> original index.
            // vec[i].second -> actual element value.
            // append only the element value to the result.
            result.push_back(vec[i].second);
        }
        // return the selected k elements in their original relative order.
        return result;
    }
};

// Time Complexity : O(Nlong)
// Space Complexity : O(N)