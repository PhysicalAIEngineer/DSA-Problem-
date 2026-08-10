// Optimal Code 
class Solution {
public:
    typedef pair<int, int> P;
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        // number of friends
        int n = times.size();
        // min heap storing occupied chairs so each element is : (depature_time, chair_number)
        priority_queue<P, vector<P>, greater<P> > occupied; 
        // min heap storing chair numbers that are currently available smllest chair number will always be at the top
        priority_queue<int, vector<int>, greater<int>> free;
        // store the arrival time of the target friends before sorting the input 
        int targetFriendArrival = times[targetFriend][0];
		// sort al friends by their arrival time so, each friend is represented as : [arrival_time, depature_time]
        sort(times.begin(),times.end());
        // new chair that has never been assigned before 
		int chairNo = 0;
        // process every friend in incresing order of arrival time
        for(int i = 0; i < n; i++) {
            // arrival time of the current friends
            int arrival  = times[i][0];
            // depature time of the current friends
            int depart   = times[i][1];
            // free all chair whose occupants have left top of the occupied heap contain the friends whose leaves earliest if their depature time <= arrival their chair is avalible for the current friends continue until every chair whose occupant has already left is moved into the free heap
            while(!occupied.empty() && occupied.top().first <= arrival) {
                // get the chair number of the friends whose leaves earliest
                free.push(occupied.top().second); 
                occupied.pop();
            }
            // case 1: no previously used chair is free 
            if(free.empty()) {
                // assign the next completely new chair to the current friends
                occupied.push({depart, chairNo});
                // check whether the current friends is the target friends
                if(arrival == targetFriendArrival)
                    // return the chair assinged to the target friends
                    return chairNo;
                // current new chair number has now beeen used so the next new chair will have the next number
                chairNo++;
            // case 2: at least one chair is avalilables
            } else {
                // smallest available chair is the top of the free min heap
                int leastChairAvailable = free.top();
                // remove the smallest chair from the free heap because are going tot assign the current friends
                free.pop();
                // check whether the current friends is the target friends
                if(arrival == targetFriendArrival) {
                    // return the smallest available chair numbers
                    return leastChairAvailable;
                }
                // chiar is occupied again by the current friends
                occupied.push({depart, leastChairAvailable});
            }
        }
        // target friends must always receive chair 
        return -1;
    }  
};

// Time Complexity : O(N)
// Space Complexity : O(N)