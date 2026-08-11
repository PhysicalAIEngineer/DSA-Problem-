// Optimal Code
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        // sort all intervals by their start times so sorting allow to process interval in the order in which they start
        sort(begin(intervals), end(intervals));
        // create a min heap, this heap stores the end time of the interval currently occupying each group 
        priority_queue<int, vector<int>, greater<int>> pq; 
        // process every interval in increasing order of start times
        for(vector<int>& interval : intervals) {
            // start and end time of the current interval.
            int start = interval[0];
            int end   = interval[1];
            // if the group whose interval ends earliest is free before this interval starts reuse that group '<' is important because intervals are closed: [1, 5] and [5, 10] overlap at 5.
            if(!pq.empty() && pq.top() < start) {
                // remove the group whose interval ended earliest that group is now avalible and can be reused for the the current interval
                pq.pop();
            }
            // add the current interval end time to the heap this mean the current interval now occupies group until end 
            pq.push(end);
        }
        // heap contain one end time for every currenlty required group therefore the number of element in the heap is the number of groups required
        return pq.size();
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)