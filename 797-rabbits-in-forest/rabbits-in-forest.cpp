// Brute Force Code & Optimal Code
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        // dictionary to store how many rabbits gave each answer
        // key   = answer x
        // value = frequency of rabbits saying x
        unordered_map<int, int> mp;
        // count the frequency of each answer
        for (int x : answers) {
            mp[x]++;
        }
        // stores the minimum total number of rabbits
        int total = 0;
        // process each unique answer and its frequency
        for (auto& [x, count] : mp) {
            // if a rabbit says x, it means there are x other rabbits having the same color so, including the rabbit itself one color group contains x + 1 rabbits.
            int groupSize = x + 1;
            // need enough groups to accommodate all rabbits that gave the same answer ceil(count / groupSize) gives the number of groups formula for ceiling division: (count + groupSize - 1) / groupSize
            int groups = (count + groupSize - 1) / groupSize;
            // each group contains groupSize rabbits so add the total rabbits from all required groups.
            total += groups * groupSize;
        }
        // return the minimum possible number of rabbits
        return total;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)