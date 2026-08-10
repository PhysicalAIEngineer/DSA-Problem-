// Brute Force Code & Optimal Code
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        long long total = 0;
        for (int s : skill) {
            total += s;
        }
        // sum of all players skills 
        int n = skill.size();
        // check if total sum can be evenly divided into n/2 teams each team has size 2, so target sum per team = (2 * total) / n
        if ((2 * total) % n != 0) {
            // cannot divide into equal total skill teams
            return -1;
        }
        // required total skill per team
        int target = (2 * total) / n;
        // count of each skill values
        unordered_map<int, int> count;
        for (int s : skill) {
            count[s]++;
        }
        // sum fot chemistry of all teams
        long long result = 0;
        // iterate over each players skill
        for (int s : skill) {
            // if count of each skill not found 
            if (count[s] == 0) {
                // already used this player in a team
                continue;
            }
            // use this player
            count[s]--;
            // if count of each skill not diffrence
            int difference = target - s;
            // if count of each skill not diffrence
            if (count[difference] == 0) {
                // no partner with the required skill exists
                return -1;
            }
            // add chemistry product of skills to result
            result += (long long)s * difference;
            // use of the patner
            count[difference]--;
        }
        // return sum of chemistry of all team
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)