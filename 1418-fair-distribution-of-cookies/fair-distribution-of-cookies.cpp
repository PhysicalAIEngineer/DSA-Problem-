// Brute Force Code & Optimal Code
class Solution {
public:
    // store the minimum unfairness found so far initially, we do not have any valid distribution so use infinity.
    int result = INT_MAX;
    // store the total number of cookies.
    int n = 0;
    void solve(int idx, vector<int>& cookies, vector<int>& children,int k) {
        // base case: if idx reaches the end of the cookies array all cookies have been distributed.
        if (idx == cookies.size()) {
            // calculate the unfairness of the current distribution unfairness is defined as the maximum number of cookies received by any child.
            int ans = *max_element(
                children.begin(),
                children.end()
            );
            // keep the minimum unfairness found among all possible distributions.
            result = min(result, ans);
            return;
        }
        // get the number of cookies represented by the current index.
        int candy = cookies[idx];
        // try giving the current cookies to every child.
        for (int i = 0; i < k; i++) {
            // give the current cookies to child i.
            children[i] += candy;
            // recursively distribute the remaining cookies move to the next cookie.
            solve(idx + 1, cookies, children, k);
            // backtracking remove the cookies from child i this restores the previous state so that the cookie can be given to another child.
            children[i] -= candy;
        }
    }
    int distributeCookies(vector<int>& cookies, int k) {
        // store the total number of cookies.
        n = cookies.size();
        // create an array representing the total cookies currently assigned to each child initially every child has 0 cookies.
        vector<int> children(k, 0);
        // start distributing cookies from index 0.
        solve(0, cookies, children, k);
        // return the minimum possible unfairness.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)