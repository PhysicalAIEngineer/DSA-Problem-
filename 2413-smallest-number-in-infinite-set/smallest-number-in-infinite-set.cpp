// Brute Force Code & Optimal Code
class SmallestInfiniteSet {
public:
    // store numbers that have been popped and later added back set keeps these numbers sorted automatically so the smallest added-back number is always at begin().
    set<int> st;
    // smallest number that has never been popped.
    int currSmallest;
    // constructor
    SmallestInfiniteSet() {
        // initially the smallest number that has never been popped is 1.
        currSmallest = 1;
    }
    int popSmallest() {
        // if there are numbers that were previously popped and then added back, the smallest one must be returned first.
        if (!st.empty()) {
            // since set is sorted begin() points to the smallest added-back number.
            int result = *st.begin();
            // remove that number from the set.
            st.erase(st.begin());
            // return the smallest available number.
            return result;
        }
        // if no number has been added back return the smallest number that has never been popped before.
        int result = currSmallest;
        // move currSmallest to the next number.
        currSmallest++;
        // return the smallest available number.
        return result;
    }
    void addBack(int num) {
        // if num >= currSmallest num has never been popped before,
        // so it is already present in the infinite set.
        if (num >= currSmallest || st.find(num) != st.end()) {
            return;
        }
        // add the previously popped number back into the available numbers.
        st.insert(num);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)