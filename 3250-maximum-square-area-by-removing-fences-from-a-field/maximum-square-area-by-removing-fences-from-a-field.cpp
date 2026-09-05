// Brute Force Code & Optimal Code
class Solution {
public:
    // modulo value to keep the result within a manageable range
    long long M = 1000000007;
    int maximizeSquareArea(int m, int n, vector<int>& hFences,vector<int>& vFences
    ) {
        // add the boundary fences horizontal boundaries are at 1 and m
        hFences.push_back(1);
        hFences.push_back(m);
        // add the boundary fences vertical boundaries are at 1 and n
        vFences.push_back(1);
        vFences.push_back(n);
        // sort the fence positions so can calculate distances between every pair
        sort(hFences.begin(), hFences.end());
        sort(vFences.begin(), vFences.end());
        // set to store all possible widths that can be created using vertical fences
        unordered_set<int> widths;
        // set to store all possible heights that can be created using horizontal fences
        unordered_set<int> heights;
        // generate all possible widths by choosing every pair of vertical fences
        for (int i = 0; i < vFences.size(); i++) {
            for (int j = i + 1; j < vFences.size(); j++) {
                // distance between two vertical fences gives a possible width
                int width = vFences[j] - vFences[i];
                // store this width set automatically removes duplicates
                widths.insert(width);
            }
        }
        // stores the largest side length that can be used for a square
        int maxSide = 0;
        // generate all possible heights by choosing every pair of horizontal fences
        for (int i = 0; i < hFences.size(); i++) {
            for (int j = i + 1; j < hFences.size(); j++) {
                // distance between two horizontal fences gives a possible height
                int height = hFences[j] - hFences[i];
                // if this height is also a possible width then can form a square
                if (widths.count(height)) {
                    // keep the largest possible side
                    maxSide = max(maxSide, height);
                }
            }
        }
        // if no common width and height were found it is impossible to make a square
        if (maxSide == 0) {
            return -1;
        }
        // area of square = side × side apply modulo to the final answer
        return (1LL * maxSide * maxSide) % M;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)