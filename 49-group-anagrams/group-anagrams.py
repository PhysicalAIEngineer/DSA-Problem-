# Optimal Code [Using Sorting]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary to map : sorted string -> list of anagrams
        mp = {}
        # traverse every string
        for string in strs:
            # sort the characters of the string all anagrams produce the same sorted key
            key = "".join(sorted(string))
            # create a new group if the key does not already exits
            if key not in mp:
                mp[key] = []
            # add the original string to its corresponding groups
            mp[key].append(string)
        # store all anagram groups
        result = []
        # collect every group from the dictionary
        for group in mp.values():
            result.append(group)
        # return all grouped anagrams
        return result 

# Time Complexity : O(Nlog)
# Space Complexity : O(N) 