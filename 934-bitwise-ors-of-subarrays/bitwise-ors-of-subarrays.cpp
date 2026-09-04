// Brute Force Code & Optimal Code
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        // stores all distinct or results of subarrays ending at the previous element
        unordered_set<int> prev;
        // temporary set for or results of subarrays ending at the current element
        unordered_set<int> curr;
        // stores all distinct or results found from every subarray
        unordered_set<int> result;
        // process each number in the array
        for (int num : arr) {
            // take every OR result from the previous position
            for (int x : prev) {
                // add the current number to the subarray and calculate its bitwise
                curr.insert(x | num);
                // store this OR result globally
                result.insert(x | num);
            }
            // start a new subarray containing only the current number
            curr.insert(num);
            // store the or result globally
            result.insert(num);
            // current or results become previous OR results for the next iteration
            prev = curr;
            // clear curr so that it can be reused for the next number
            curr.clear();
        }
        // return the number of distinct bitwise OR results
        return result.size();
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)