# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # set to store all original words used for checking exact matches
        self.exactWords = set() 
        # dictionary to store: lowercase word -> original word
        self.caseMap = {} 
        # dictionary to store: vowel-masked word -> original word
        self.vowelMap = {} 
    def toLower(self, s): 
        # convert the entire string to lowercase
        return s.lower() 
    def maskVowels(self, s): 
        # replace every vowel with '*'
        res = list(s) 
        # check every character in the string
        for i in range(len(res)): 
            # if the character is a vowel replace it with '*'
            if res[i] in "aeiou": 
                res[i] = '*' 
        # convert the list back into a string
        return ''.join(res) 
    def checkForMatch(self, query): 
        # check for an exact match if the query exists exactly in wordlist return the query itself
        if query in self.exactWords: 
            return query 
        # check for a case-insensitive match convert query to lowercase
        lowerQuery = self.toLower(query) 
        # check whether the lowercase version exists in the caseMap
        if lowerQuery in self.caseMap: 
            # return the original word from wordlist
            return self.caseMap[lowerQuery] 
        # check for a vowel-error match convert all vowels of the lowercase query into '*'
        maskedQuery = self.maskVowels(lowerQuery) 
        # check whether this masked pattern exists in the vowelMap
        if maskedQuery in self.vowelMap: 
            # return the original word from wordlist
            return self.vowelMap[maskedQuery] 
        # no match found
        return "" 
    def spellchecker(self, wordlist, queries): 
        # clear the maps in case the same Solution object is used for multiple test cases
        self.exactWords.clear() 
        self.caseMap.clear() 
        self.vowelMap.clear() 
        # build all lookup maps using wordlist
        for word in wordlist: 
            # store the original word for exact matching
            self.exactWords.add(word) 
            # convert the word to lowercase
            lowerWord = self.toLower(word) 
            # if this lowercase word is not already stored store the first occurrence
            if lowerWord not in self.caseMap: 
                self.caseMap[lowerWord] = word 
            # convert the lowercase word into its vowel-masked form
            maskedWord = self.maskVowels(lowerWord) 
            # store only the first word having this vowel pattern
            if maskedWord not in self.vowelMap: 
                self.vowelMap[maskedWord] = word 
        # store the final answer for all queries
        result = [] 
        # process every query
        for query in queries:
            # find the best matching word and add it to the result
            result.append(self.checkForMatch(query)) 
        # return the answers for all queries
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)