// Brute Force Code & Optimal Code
class Solution {
public:
    // sort characters in decreasing order of frequency characters that appear more frequently should get positions requiring fewer pushes.
    vector<char> sortFunc(string word) {
        // store the frequency of every character.
        unordered_map<char, int> mp;
        // count how many times each character appears.
        for (char ch : word) {
            mp[ch]++;
        }
        // convert string into a vector of characters.
        vector<char> result(word.begin(), word.end());
        // sort all characters by their frequency from highest to lowest.
        sort(result.begin(), result.end(),
            [&](char a, char b) {
                return mp[a] > mp[b];
            });
        // return the characters sorted by decreasing frequency.
        return result;
    }
    int minimumPushes(string word) {
        // there are 8 available keys: 2, 3, 4, 5, 6, 7, 8, 9 if there are 8 or fewer characters every character can be assigned to its own key and needs only 1 push.
        if (word.length() <= 8) {
            return word.length();
        }
        // sort characters by decreasing frequency this ensures that characters appearing more often are assigned to positions requiring fewer pushes.
        vector<char> sortedWord = sortFunc(word);
        // myMap[key] stores the different characters assigned to that key.
        unordered_map<int, unordered_set<char>> myMap;
        // mp[character] = {key, position}
        unordered_map<char, pair<int, int>> mp;
        // store the total number of pushes.
        int result = 0;
        // start assigning new characters from key 2.
        int assign = 2;
        // process characters in decreasing frequency order.
        for (char ch : sortedWord) {
            // there are only 8 keys: 2 to 9 after key 9, start again from key 2.
            if (assign > 9) {
                assign = 2;
            }
            // assign the character only the first time encounter it.
            if (mp.find(ch) == mp.end()) {
                // create an empty set for the key if this key has not been used yet.
                if (myMap.find(assign) == myMap.end()) {
                    myMap[assign] = unordered_set<char>();
                }
                // assign the new character to this key.
                myMap[assign].insert(ch);
                // number of characters currently assigned to this key determines the number of pushes.
                // 1st character -> 1 push
                // 2nd character -> 2 pushes
                // 3rd character -> 3 pushes
                // 4th character -> 4 pushes
                int position = myMap[assign].size();
                // store the key and push count for this character.
                mp[ch] = {assign, position};
                // add the push count for this occurrence.
                result += position;
                // move to the next key for the next new character.
                assign++;
            }
            else {
                // character has already been assigned to a key every occurrence of the same character requires the same number of pushes.
                result += mp[ch].second;
            }
        }
        // return the minimum total number of pushes.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)