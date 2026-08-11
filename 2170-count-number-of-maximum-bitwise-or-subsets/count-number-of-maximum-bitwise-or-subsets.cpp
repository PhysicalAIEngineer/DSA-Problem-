// Brute Force Code
class Solution {
private:
    // store the maximum bitwise or found so far. initially, no elements have been selected so the or value starts at 0.
    int maximum_or = 0;
    // store the number of subsets that have the maximum OR value found so far
    int count = 0;
    // generate all possible subsets using backtracking at every element, we have two choices: 1. include the current element and 2. do not include the current element this generates every possible subset.
    void backtrack(int index, int current_or, int chosen, const std::vector<int>& nums) {
        // Base case : if index reaches the length of nums have processed every element therefore, the current subset is complete.
        if (index == nums.size()) {
            // ignore the empty subset chosen represents how many elements were included in the current subset.
            if (chosen == 0) {
                return;
            }
            // found a new maximum OR if the OR of the current subset is greater than the maximum OR seen so far
            if (current_or > maximum_or) {
                // update the maximum OR.
                maximum_or = current_or;
                // since this is the new maximum all previous subsets are no longer considered maximum current subset is the first subset having this new maximum OR.
                count = 1;
            // found another subset with same maximum if the current subset has exactly the same OR as the maximum OR
            } else if (current_or == maximum_or) {
                count += 1;
            }
            // current subset has been processed.
            return;
        }
        // Choice 1: include nums[index]
        // add nums[index] to the current subset.
        // update the OR: current_or | nums[index]
        // also increase chosen because selected one more element.
        backtrack(index + 1, current_or | nums[index], chosen + 1, nums);
        // Choice 2: Do not include nums[index]
        // leave current_or unchanged because nums[index] is not selected chosen also remains unchanged.
        backtrack(index + 1, current_or, chosen, nums);
    }

public:
    int countMaxOrSubsets(std::vector<int>& nums) {
        // store the maximum bitwise or found so far. initially, no elements have been selected so the or value starts at 0.
        maximum_or = 0;
        // store the number of subsets that have the maximum OR value found so far
        count = 0;
        // start generating subsets
        // 1. index = 0  → start from the first element.
        // 2. current_or = 0 → no elements have been selected yet.
        // 3. chosen = 0 → The current subset is empty.
        backtrack(0, 0, 0, nums);
        // return the number of non-empty subsets whose bitwise OR is equal to the maximum OR.
        return count;
    }
};

// Time Complexity : O(N!)
// Space Complexity : O(N)