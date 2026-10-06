// Brute Force Code & Optimal Code
using namespace std;
class Solution {
public:
    // store the expression
    string s;
    // length of the expression
    int n = 0;
    // current index while parsing the expression
    int idx = 0;
    set<string> getunit() {
        // store all possible strings for the current unit
        set<string> result;
        // if current character is "{" process everything inside the braces
        if (s[idx] == '{') {
            idx++;
            // process the content inside {}
            result = performunion();
        } else {
            // current character is a single alphabet
            result.insert(string(1, s[idx]));
        }
        // move index to the next character
        idx++;
        return result;
    }
    set<string> performConcat() {
        // start with an empty string so that first unit can be concatenated
        set<string> result;
        result.insert("");
        // continue while there are characters that can start a new unit
        while (idx < n && (s[idx] == '{' || isalpha(s[idx]))) {
            // get all possible strings for the current unit
            set<string> temp = getunit();
            // store all possible concatenated strings
            set<string> concatresult;
            // combine every string from result with every string from temp
            for (string left : result) {
                for (string right : temp) {
                    concatresult.insert(left + right);
                }
            }
            // update result with newly generated strings
            result = concatresult;
        }
        return result;
    }
    set<string> performunion() {
        // store all possible strings from union
        set<string> result;
        while (true) {
            // process one concatenation part
            set<string> temp = performConcat();
            // add all generated strings to result
            result.insert(temp.begin(), temp.end());
            // if "," is found move to the next union part
            if (idx < n && s[idx] == ',') {
                idx++;
            } else {
                // no more union parts
                break;
            }
        }
        return result;
    }
    vector<string> braceExpansionII(string expression) {
        // store expression and its length
        n = expression.length();
        s = expression;
        // start parsing from index 0
        idx = 0;
        // process the complete expression
        set<string> start = performunion();
        // set already stores strings in sorted order
        vector<string> result(
            start.begin(),
            start.end()
        );
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)