// Brute Force Code & Optimal Code
class Solution {
public:
    // set to store all original words used for checking exact matches
    unordered_set<string> exactWords;
    // dictionary to store: lowercase word -> original word
    unordered_map<string, string> caseMap;
    // dictionary to store: vowel-masked word -> original word
    unordered_map<string, string> vowelMap;
    string toLower(string s) {
        // convert the entire string to lowercase
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        return s;
    }
    string maskVowels(string s) {
        // replace every vowel with '*'
        string res = s;
        // check every character in the string
        for (int i = 0; i < res.length(); i++) {
            // if the character is a vowel replace it with '*'
            if (res[i] == 'a' || res[i] == 'e' || res[i] == 'i' ||res[i] == 'o' || res[i] == 'u') {
                res[i] = '*';
            }
        }
        // return the vowel-masked string
        return res;
    }
    string checkForMatch(string query) {
        // check for an exact match if the query exists exactly in wordlist return the query itself
        if (exactWords.count(query)) {
            return query;
        }
        // check for a case-insensitive match convert query to lowercase
        string lowerQuery = toLower(query);
        // check whether the lowercase version exists in the caseMap
        if (caseMap.count(lowerQuery)) {
            // return the original word from wordlist
            return caseMap[lowerQuery];
        }
        // check for a vowel-error match convert all vowels of the lowercase query into '*'
        string maskedQuery = maskVowels(lowerQuery);
        // check whether this masked pattern exists in the vowelMap
        if (vowelMap.count(maskedQuery)) {
            // return the original word from wordlist
            return vowelMap[maskedQuery];
        }
        // no match found
        return "";
    }
    vector<string> spellchecker(vector<string>& wordlist,vector<string>& queries
    ) {
        // clear the maps in case the same Solution object is used for multiple test cases
        exactWords.clear();
        caseMap.clear();
        vowelMap.clear();
        // build all lookup maps using wordlist
        for (string& word : wordlist) {
            // store the original word for exact matching
            exactWords.insert(word);
            // convert the word to lowercase
            string lowerWord = toLower(word);
            // if this lowercase word is not already stored store the first occurrence
            if (!caseMap.count(lowerWord)) {
                caseMap[lowerWord] = word;
            }
            // convert the lowercase word into its vowel-masked form
            string maskedWord = maskVowels(lowerWord);
            // store only the first word having this vowel pattern
            if (!vowelMap.count(maskedWord)) {
                vowelMap[maskedWord] = word;
            }
        }
        // store the final answer for all queries
        vector<string> result;
        // process every query
        for (string& query : queries) {
            // find the best matching word and add it to the result
            result.push_back(checkForMatch(query));
        }
        // return the answers for all queries
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)