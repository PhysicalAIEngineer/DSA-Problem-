// Brute Force Code & Optimal Code
class Solution {
public:
    // recursive function to compute all possible results
    vector<int> solve(string expression) {
        // store every possible result for the current expression
        vector<int> result;
        // traverse every character in the expression
        for (int i = 0; i < expression.length(); i++) {
            // if the current character is an operator, split the expression into two parts
            if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
                // recursively compute all possible results for the left sub-expression
                vector<int> left_results =
                    solve(expression.substr(0, i));
                // recursively compute all possible results for the right sub-expression
                vector<int> right_results =
                    solve(expression.substr(i + 1));
                // combine every possible left result with every possible right result
                for (int left : left_results) {
                    for (int right : right_results) {
                        // apply the current operator
                        if (expression[i] == '+') {
                            result.push_back(left + right);
                        }
                        else if (expression[i] == '-') {
                            result.push_back(left - right);
                        }
                        else {
                            // '*'
                            result.push_back(left * right);
                        }
                    }
                }
            }
        }
        // if no operator exists in the expression it represents a single number
        if (result.empty()) {
            result.push_back(stoi(expression));
        }
        // return all possible results for the current expression
        return result;
    }
    // Return every possible result obtained
    // by placing parentheses in different ways
    vector<int> diffWaysToCompute(string expression) {
        // start the recursive divide-and-conquer process
        return solve(expression);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)