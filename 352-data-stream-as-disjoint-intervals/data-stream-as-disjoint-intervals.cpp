// Brute Force Code & Optimal Code
class SummaryRanges {
public:
    // store all unique numbers from the data stream in sorted order.
    set<int> st;
    // add a number to the data stream.
    void addNum(int value) {
        // insert the number into the sorted set automatically:
        // 1. keeps elements sorted.
        // 2. ignores duplicate values.
        st.insert(value);
    }
    // return the summary of disjoint intervals.
    vector<vector<int>> getIntervals() {
        // store the resulting intervals.
        vector<vector<int>> result;
        // if there are no numbers, return an empty result.
        if (st.empty()) {
            return result;
        }
        // iterator to traverse the sorted numbers.
        auto it = st.begin();
        // start of the current interval.
        int start = *it;
        // previous number in the current interval.
        int previous = *it;
        // move through all numbers in sorted order.
        ++it;
        while (it != st.end()) {
            // current number.
            int current = *it;
            // if current and previous are consecutive they belong to the same interval.
            if (previous + 1 == current) {
                previous = current;
            }
            else {
                // consecutive sequence has ended store the current interval.
                result.push_back({start, previous});
                // start a new interval.
                start = current;
                previous = current;
            }
            // move to the next number.
            ++it;
        }
        // store the final interval.
        result.push_back({start, previous});
        // return all disjoint intervals.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)