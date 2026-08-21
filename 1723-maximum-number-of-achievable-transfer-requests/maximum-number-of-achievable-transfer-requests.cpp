// Brute Force Code & Optimal Code
class Solution {
public:
    // store the total number of requests.
    int m = 0;
    // store the maximum number of accepted requests from all valid combinations found so far initially, no valid combination has been found so use negative infinity.
    int result = INT_MIN;
    void solve(int idx, int count, int n, vector<int>& resultant,vector<vector<int>>& requests) {
        // base case: if all requests have been considered, check whether the current selection of requests is valid.
        if (idx == m) {
            // assume every building is balanced when the number of people entering it equals the number of people leaving it.
            bool allZero = true;
            // check the net change of every building.
            for (int x : resultant) {
                // if any building has a non-zero net change the selected requests are invalid.
                if (x != 0) {
                    allZero = false;
                    break;
                }
            }
            // if every building has net change 0 this is a valid combination of requests.
            if (allZero) {
                // keep the maximum number of accepted requests found so far.
                result = max(result, count);
            }
            return;
        }
        // get the current request.
        // 1. from_building -> building where the person currently is.
        // 2. to            -> building where the person wants to go.
        int from_building = requests[idx][0];
        int to = requests[idx][1];
        // option 1: accept the current request one person leaves the source building therefore its number of people decreases by 1.
        resultant[from_building]--;
        // one person enters the destination building therefore its number of people increases by 1.
        resultant[to]++;
        // recursively process the next request since we accepted this request increase the accepted request count by 1.
        solve(idx + 1, count + 1, n, resultant, requests);
        // backtracking: undo the changes caused by accepting the current request restore the source building.
        resultant[from_building]++;
        // restore the destination building.
        resultant[to]--;
        // option 2: reject the current request do not modify resultant because the request is not accepted simply move to the next request.
        solve(idx + 1, count, n, resultant, requests);
    }
    int maximumRequests(int n, vector<vector<int>>& requests) {
        // store the total number of requests.
        m = requests.size();
        // resultant[i] stores the net change in the number of people at building i.
        // 1. positive value -> more people entered.
        // 2. negative value -> more people left.
        // 3. zero          -> balanced.
        vector<int> resultant(n, 0);
        // start considering requests from index 0 initially count = 0 because no requests have been accepted.
        solve(0,0,n,resultant,requests);
        // return the maximum number of requests that can be accepted while keeping every building balanced.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)