// Brute Force Code & Optimal Code
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // store (frequency, word) pairs
        vector<pair<int, string>> vec_str;
        // dictionary to count frequency of each word
        unordered_map<string, int> mp;
        // count frequency of every word
        for (string& word : words) {
            mp[word]++;
        }
        // store (frequency, word) pairs in the vector
        for (auto& it : mp) {
            vec_str.push_back({it.second, it.first});
        }
        // sort by frequency in descending order if frequencies are equal, sort words alphabetically
        sort(vec_str.begin(), vec_str.end(),
             [](const pair<int, string>& p1, const pair<int, string>& p2) {
                 if (p1.first != p2.first) {
                     return p1.first > p2.first;
                 }
                 return p1.second < p2.second;
             });
        // store the top k frequent words
        vector<string> result;
        int i = 0;
        // continue until k words are selected
        while (i < k) {
            // add the word from the current pair
            result.push_back(vec_str[i].second);
            i++;
        }
        // return the k most frequent words
        return result;
    }
};

// Time Complexity : O(NlogN)
// Space Complexity : O(N)
