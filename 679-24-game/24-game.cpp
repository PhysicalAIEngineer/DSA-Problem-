// Brute Force Code & Optimal Code
class Solution {
public:
    // store a small tolerance value for comparing floating-point numbers with 24.
    double epsilon = 0.1;
    bool solve(vector<double>& cards) {
        // base case: if only one number remains all operations have been completed.
        if (cards.size() == 1) {
            // check whether the remaining value is close enough to 24.
            return abs(cards[0] - 24) <= epsilon;
        }
        // try every number as the first operand.
        for (int i = 0; i < cards.size(); i++) {
            // try every number as the second operand.
            for (int j = 0; j < cards.size(); j++) {
                // same element cannot be used twice.
                if (i == j) {
                    continue;
                }
                // store all numbers except cards[i] and cards[j].
                vector<double> temp;
                for (int k = 0; k < cards.size(); k++) {
                    // keep numbers that were not selected.
                    if (k != i && k != j) {
                        temp.push_back(cards[k]);
                    }
                }
                // select the two numbers.
                double a = cards[i];
                double b = cards[j];
                // store all possible results obtained by combining a and b addition and multiplication are commutative while subtraction and division need both orders.
                vector<double> possibleVal = {a + b, a - b, b - a, a * b};
                // try a / b if b is not zero.
                if (abs(b) > 0.0) {
                    possibleVal.push_back(a / b);
                }
                // try b / a if a is not zero.
                if (abs(a) > 0.0) {
                    possibleVal.push_back(b / a);
                }
                // try every possible result of combining the selected pair.
                for (double val : possibleVal) {
                    // DO / CHOOSE
                    // add the result of the chosen operation to the remaining numbers.
                    temp.push_back(val);
                    // EXPLORE
                    // Two numbers have been replaced by one result so the number of elements decreases by one.
                    if (solve(temp)) {
                        // way to make 24 has been found.
                        return true;
                    }
                    // UNDO / BACKTRACK
                    // remove the operation result so that another operation can be tried.
                    temp.pop_back();
                }
            }
        }
        // if every pair and every operation has been tried and none can produce 24, return false.
        return false;
    }
    bool judgePoint24(vector<int>& cards) {
        // convert all integers to floating-point numbers floating-point values are needed because division may produce decimal results.
        vector<double> nums;
        for (int card : cards) {
            nums.push_back((double)card);
        }
        // start the backtracking process with all cards returns true if some combination of operations can produce 24.
        return solve(nums);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)