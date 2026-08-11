// Brute Force Code & Optimal Code
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        // dictionary to store the longest square streak
        unordered_map<int, int> mp;
        // sort the array in increasing order 
        sort(begin(nums), end(nums));
        // store the logest square streak found so far
        int maxStreak = 0;
        // process every number in sorted order
        for(int &num : nums) {
            // calculte the interger square root of num
            int root = (int)sqrt(num);
            // check whether num is perfect square
            if(root*root == num && mp.find(root) != mp.end()) {
                // extend the square streak that ends
                mp[num] = mp[root] + 1;
            } else {
                // if num is not the square of previously processed number start new steak 
                mp[num] = 1;
            }
            // update the longest streak found so far
            maxStreak = max(maxStreak, mp[num]);
        }
        // valid square sterak must contain at least two numbers
        return maxStreak < 2 ? -1 : maxStreak;
    }
};

// Time Complexity : O(Nlog)
// Space Complexity : O(N)