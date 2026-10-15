// Brute Force Code & Optimal Code
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        // store all valid genetic sequences in a set for fast lookup
        unordered_set<string> valid_genetic_sequence(
            bank.begin(), bank.end()
        );
        // track visited genetic sequences to avoid revisiting them
        unordered_set<string> track_visited_genetic_sequence;
        // create a queue for BFS
        queue<string> q;
        // add the starting genetic sequence to the queue and mark it visited
        q.push(start);
        track_visited_genetic_sequence.insert(start);
        // count the number of mutations performed
        int number_mutations_performed = 0;
        // perform BFS until the queue becomes empty
        while (!q.empty()) {
            // number of sequences at the current BFS level
            int number_sequence = q.size();
            // process all sequences at the current level
            while (number_sequence--) {
                // remove the front genetic sequence from the queue
                string remove_front_genetic_sequence = q.front();
                q.pop();
                // if the target sequence is reached, return the mutation count
                if (remove_front_genetic_sequence == end) {
                    return number_mutations_performed;
                }
                // try changing each character to A, C, G, or T
                for (char character : string("ACGT")) {
                    // try changing every position in the current sequence
                    for (int i = 0;
                         i < remove_front_genetic_sequence.length();
                         i++) {
                        // create a new genetic sequence by changing one character
                        string new_genetic_sequence =
                            remove_front_genetic_sequence;
                        new_genetic_sequence[i] = character;
                        // check whether the new sequence is valid and unvisited
                        if (track_visited_genetic_sequence.find(
                                new_genetic_sequence
                            ) == track_visited_genetic_sequence.end() &&
                            valid_genetic_sequence.find(
                                new_genetic_sequence
                            ) != valid_genetic_sequence.end()) {
                            // mark the new sequence as visited
                            track_visited_genetic_sequence.insert(
                                new_genetic_sequence
                            );
                            // add it to the queue for further exploration
                            q.push(new_genetic_sequence);
                        }
                    }
                }
            }
            // increase the mutation count after processing one BFS level
            number_mutations_performed++;
        }
        // return -1 if the target sequence cannot be reached
        return -1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)