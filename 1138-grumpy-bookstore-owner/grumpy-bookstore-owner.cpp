// Brute Force Code & Optimal Code
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        // length of the array
        int n = customers.size();
        // store unsatisfied customers in current window
        int unsatisfied = 0;
        // calculate unsatisfied customers in the first 'minutes' window
        for (int i = 0; i < minutes; i++) {
            unsatisfied += customers[i] * grumpy[i];
        }
        // assume first window gives maximum unsatisfied customers that can be saved
        int maxunsatisfied = unsatisfied;
        // sliding window of size minutes
        int i = 0;
        int j = minutes;
        while (j < n) {
            // add customers from the new position if the owner is grumpy
            unsatisfied += customers[j] * grumpy[j];
            // remove customers from the old position
            unsatisfied -= customers[i] * grumpy[i];
            // store maximum customers that can be saved
            maxunsatisfied = max(maxunsatisfied, unsatisfied);
            // move window forward
            i++;
            j++;
        }
        // start with maximum customers that can be made satisfied using the secret technique
        int totalcustomers = maxunsatisfied;
        // add customers who are already satisfied because grumpy[i] == 0
        for (int i = 0; i < n; i++) {
            totalcustomers += customers[i] * (1 - grumpy[i]);
        }
        // return maximum satisfied customers
        return totalcustomers;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)