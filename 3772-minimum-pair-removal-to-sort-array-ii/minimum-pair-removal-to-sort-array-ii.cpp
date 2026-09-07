// Brute Force Code & Optimal Code
class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        // store the size of the array
        int n = nums.size();
        // copy nums into temp temp will store the current value of each element
        // example: {a, b, c, d} -> {a, b, c, d}
        vector<long long> temp(n);
        for (int i = 0; i < n; i++) {
            temp[i] = nums[i];
        }
        // store all adjacent pairs as: (sum of pair, index of first element)
        set<pair<long long, int>> minPairSet;
        // nextIndex[i] = index of the next active element
        // prevIndex[i] = index of the previous active element
        // these arrays help us simulate deleting/merging elements without actually shifting the array
        vector<int> nextIndex(n);
        vector<int> prevIndex(n);
        for (int i = 0; i < n; i++) {
            nextIndex[i] = i + 1;
            prevIndex[i] = i - 1;
        }
        // count adjacent pairs that violate the non-decreasing order
        // example: [1, 5, 3] pair (5, 3) is bad because 5 > 3
        int badPairs = 0;
        // add every adjacent pair to the set
        for (int i = 0; i < n - 1; i++) {
            // if left value > right value this pair is not in sorted order
            if (temp[i] > temp[i + 1]) {
                badPairs++;
            }
            // store pair sum and its first index
            minPairSet.insert({temp[i] + temp[i + 1], i});
        }
        // count how many merge operations we perform
        int operations = 0;
        // continue until there are no bad adjacent pairs i.e. the array becomes non-decreasing
        while (badPairs > 0) {
            // get the pair having the minimum sum set stores pairs in sorted order so begin() gives the smallest pair
            int first = minPairSet.begin()->second;
            // second element of the pair
            int second = nextIndex[first];
            // element just before the pair
            int first_left = prevIndex[first];
            // element just after the pair
            int second_right = nextIndex[second];
            // remove the selected minimum-sum pair
            minPairSet.erase(minPairSet.begin());
            // if the selected pair itself was a bad pair removing it decreases the bad pair count
            if (temp[first] > temp[second]) {
                badPairs--;
            }
            // check the pair on the left side so before: {d, (a, b)} and after merging: {d, (a+b)}
            if (first_left >= 0) {
                // previously bad: d > a and  after merging: d <= a+b so this pair becomes good
                if (temp[first_left] > temp[first] && temp[first_left] <= temp[first] + temp[second]) {
                    badPairs--;
                }
                // previously good: d <= a and  after merging: d > a+b so this pair becomes bad
                else if (temp[first_left] <= temp[first] && temp[first_left] > temp[first] + temp[second]) {
                    badPairs++;
                }
            }
            // check the pair on the right side so before: {(a, b), d} and  after merging: {(a+b), d}
            if (second_right < n) {
                // previously good: b <= d and  after merging: a+b > d so this pair becomes bad
                if (temp[second_right] >= temp[second] && temp[second_right] < temp[first] + temp[second]) {
                    badPairs++;
                }
                // previously bad: b > d and after merging: a+b <= d so this pair becomes good
                else if (temp[second_right] < temp[second] && temp[second_right] >= temp[first] + temp[second]) {
                    badPairs--;
                }
            }
            // update the pair on the left so old pair was: (d, a) and  after merging: (d, a+b)
            if (first_left >= 0) {
                // remove the old left pair
                minPairSet.erase({temp[first_left] + temp[first],first_left});
                // add the new left pair with the merged value
                minPairSet.insert({temp[first_left] + temp[first] + temp[second],first_left
                });
            }
            // update the pair on the right so old pair was: (b, d) and  after merging: (a+b, d)
            if (second_right < n) {
                // remove the old right pair
                minPairSet.erase({temp[second] + temp[second_right],second});
                // add the new right pair the merged element is stored at index 'first'
                minPairSet.insert({
                    temp[first] + temp[second] + temp[second_right],
                    first
                });
                // previous active element of second_right is now 'first'
                prevIndex[second_right] = first;
            }
            // next active element after 'first' is now whatever came after 'second'
            nextIndex[first] = second_right;
            // merge second element into first
            temp[first] += temp[second];
            // one pair-removal operation is completed
            operations++;
        }
        // return the minimum number of operations required to make the array non-decreasing
        return operations;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)