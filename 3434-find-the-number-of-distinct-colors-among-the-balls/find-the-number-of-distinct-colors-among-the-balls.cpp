// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        // number of queries need to store the answer after every query.
        int n = queries.size();
        // result[i] stores the number of distinct colors present on the balls after processing queries[i].
        vector<int> result(n, 0);
        // colormp[color] = number of balls currently having the color.
        unordered_map<int, int> colormp;
        // ballmp[ball] = current color of that ball.
        unordered_map<int, int> ballmp;
        // Process every query one by one.
        for (int i = 0; i < n; i++) {
            // extract the ball number and new color from the current query.
            int ball = queries[i][0];
            int color = queries[i][1];
            // check whether this ball already has a color.
            if (ballmp.find(ball) != ballmp.end()) {
                // get the color that the ball had before.
                int prevcolor = ballmp[ball];
                // since this ball is changing its color it should no longer be counted under its previous color.
                colormp[prevcolor]--;
                // if no other ball has the previous color remove the color completely this is important because colormp.size() represents the number of distinct colors.
                if (colormp[prevcolor] == 0) {
                    colormp.erase(prevcolor);
                }
            }
            // assign the new color to the ball if the ball already existed, its old color has already been removed above.
            ballmp[ball] = color;
            // increase the number of balls having the new color.
            colormp[color]++;
            // number of keys in colormp is exactly the number of distinct colors currently present.
            result[i] = colormp.size();
        }
        // return the number of distinct colors after every query.
        return result;
    }
};

// Time Complexity : O(N)
// Space COmplexity : O(N)