// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> partitionLabels(string s) {
        // total number of characters in the string
        int n = s.length();
        // list to store the size of each partition
        vector<int> result;
        // array to store the last occurrence of every lowercase character
        vector<int> last_occurrence(26, -1);
        // record the last index of each character
        for (int i = 0; i < n; i++) {
            int index = s[i] - 'a';
            last_occurrence[index] = i;
        }
        // initialize pointers current_index -> current position in the string
        int current_index = 0;
        // partition_start -> starting index of the current partition
        int partition_start = 0;
        // partition_end -> farthest index the current partition must reach
        int partition_end = 0;
        // traverse the string
        while (current_index < n) {
            // extend the partition to include the last occurrence of the current character
            partition_end = max(partition_end, last_occurrence[s[current_index] - 'a']);
            // if the current index reaches the partition's end record its size and start a new partition
            if (current_index == partition_end) {
                result.push_back(partition_end - partition_start + 1);
                // next partition starts after the current partition
                partition_start = partition_end + 1;
            }
            // move to the next character
            current_index++;
        }
        // return the sizes of all partitions
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)