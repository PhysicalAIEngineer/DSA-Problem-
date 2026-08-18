// Brute Force Code & Optimal Code
class Solution {
public:
    // words for numbers from 0 to 9
    unordered_map<int, string> below_ten = {{0, ""},{1, "One"},{2, "Two"},{3, "Three"},{4, "Four"},
    {5, "Five"},{6, "Six"},{7, "Seven"},{8, "Eight"},
    {9, "Nine"}
    };
    // words for numbers from 10 to 19
    unordered_map<int, string> below_twenty = {{10, "Ten"},{11, "Eleven"},{12, "Twelve"},{13, "Thirteen"},{14, "Fourteen"},{15, "Fifteen"},
    {16, "Sixteen"},{17, "Seventeen"},{18, "Eighteen"},
    {19, "Nineteen"}
    };
    // eords for multiples of ten 20, 30, 40, ..., 90
    unordered_map<int, string> below_hundred = {{1, "Ten"},{2, "Twenty"},{3, "Thirty"},{4, "Forty"},{5, "Fifty"},{6, "Sixty"},{7, "Seventy"},{8, "Eighty"},{9, "Ninety"}
    };
    // recursive function to convert a number into words
    string solve(long long num) {
        // case 1: numbers from 0 to 9
        if (num < 10) {
            return below_ten[num];
        }
        // case 2: numbers from 10 to 19
        if (num < 20) {
            return below_twenty[num];
        }
        // case 3: numbers from 20 to 99
        if (num < 100) {
            string result = below_hundred[num / 10];
            if (num % 10 != 0) {
                result += " " + below_ten[num % 10];
            }
            return result;
        }
        // case 4: numbers from 100 to 999
        if (num < 1000) {
            string result = solve(num / 100) + " Hundred";
            if (num % 100 != 0) {
                result += " " + solve(num % 100);
            }
            return result;
        }
        // case 5: numbers from 1,000 to 999,999
        if (num < 1000000) {
            string result = solve(num / 1000) + " Thousand";
            if (num % 1000 != 0) {
                result += " " + solve(num % 1000);
            }
            return result;
        }
        // case 6: numbers from 1,000,000 to 999,999,999
        if (num < 1000000000) {
            string result = solve(num / 1000000) + " Million";
            if (num % 1000000 != 0) {
                result += " " + solve(num % 1000000);
            }
            return result;
        }
        // case 7: Numbers from 1,000,000,000 and above
        string result = solve(num / 1000000000) + " Billion";
        if (num % 1000000000 != 0) {
            result += " " + solve(num % 1000000000);
        }
        return result;
    }
    // main function to convert a number into English words
    string numberToWords(int num) {
        // special case: 0
        if (num == 0) {
            return "Zero";
        }
        // convert the number recursively
        return solve(num);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)

// Time Complexity : O(N)
// Space Complexity : O(1)