// Brute Force Code & Optimal Code
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // add the new interval to the existing list
        intervals.push_back(newInterval);
        // sort all intervals by their starting points
        sort(intervals.begin(), intervals.end());
        // store the final merged intervals
        vector<vector<int>> result;
        // traverse every interval
        for (vector<int>& interval : intervals) {
            // if this is the first interval add it directly
            if (result.empty()) {
                result.push_back(interval);
            }
            else {
                // get the last merged interval
                vector<int>& last_interval = result.back();
                // check whether the current interval overlaps with the last merged interval
                if (interval[0] <= last_interval[1]) {
                    // merge the intervals by extending the ending point
                    last_interval[1] = max(last_interval[1], interval[1]);
                }
                else {
                    // no overlap, start a new interval
                    result.push_back(interval);
                }
            }
        }
        // return the merged intervals
        return result;
    }
};

// Time Complexity : O(Nlog)
// Space Complexity : O(1)