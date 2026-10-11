# Brute Force Code & Optimal Code
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # store (frequency, word) of pairs
        vec_str = []
        # dictionary to count frequency of each word
        mp = {}
        # count frequency of every word
        for word in words:
            mp[word] = mp.get(word, 0) + 1
        # store (frequency, word) pairs in the list
        for word, freq in mp.items():
            vec_str.append((freq, word))
        # sort by frequnecy in descening order if frequencies are equal sort words alphabetically
        vec_str.sort(key = lambda p: (-p[0], p[1]))
        # store the top k frequenct words
        result = []
        i = 0
        # continue until the k 
        while i < k:
            # add the words from the current pairs
            result.append(vec_str[i][1])
            i += 1
        # return the k most frequent words
        return  result 