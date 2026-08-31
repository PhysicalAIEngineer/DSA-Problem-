// Brute Force Code & Optimal Code
class Solution {
public:
    string findRoot(string word, unordered_set<string>& st) {
        // try every possible prefix of the current word start from length 1 because want to find the shortest possible root.
        for (int l = 1; l <= word.length(); l++) {
            // take the first l characters of the word.
            string root = word.substr(0, l);
            // check whether this prefix exists in the dictionary set since check prefixes from shortest to longest the first match is the shortest root.
            if (st.find(root) != st.end()) {
                return root;
            }
        }
        // if no prefix of the word exists in the dictionary keep the original word unchanged.
        return word;
    }
    string replaceWords(vector<string>& dictionary, string sentence) {
        // convert the dictionary list into a set.
        unordered_set<string> st;
        for (string word : dictionary) {
            st.insert(word);
        }
        // split the sentence into individual words.
        stringstream ss(sentence);
        // store the final words after replacing them with their shortest roots.
        vector<string> result;
        // process every word in the sentence.
        string word;
        while (ss >> word) {
            // find the shortest dictionary root for the current word.
            string root = findRoot(word, st);
            // add the root to the result.
            result.push_back(root);
        }
        // join all processed words with a single space.
        string answer = "";
        for (int i = 0; i < result.size(); i++) {
            // add a space between words.
            if (i > 0) {
                answer += " ";
            }
            // add the processed word.
            answer += result[i];
        }
        // return the final sentence.
        return answer;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)