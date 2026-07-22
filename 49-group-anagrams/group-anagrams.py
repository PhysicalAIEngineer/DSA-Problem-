# Optimal Code [Without Sorting]
class Solution:
    # generate a canonical representation of string using characters frequencies
    def generate(self, s: str):
        # frequency of array for characters "a" to "z"
        count = [0] * 26
        # count the frequency of each chracters
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        # bulid the canonical string from the frequency array
        new_string = []
        for i in range(26):
            # append each characters according to its frequency
            if count[i] > 0:
                new_string.append(chr(i + ord("a")) * count[i])
        # return the canonical string
        return "".join(new_string)
    # group all anagrams togethers
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary to map : canonical string -> list of anagrams
        mp = {}
        # process every string
        for s in strs:
            # generate the canonical key
            key = self.generate(s)
            # create a new group if the key is not presents
            if key not in mp:
                mp[key] = []
            # add the original string to its anagrams groups
            mp[key].append(s)
        # store all grouped anagrams
        result = []
        # collect every groups from the dictionary
        for group in mp.values():
            result.append(group)
        # return all anagram groups
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)