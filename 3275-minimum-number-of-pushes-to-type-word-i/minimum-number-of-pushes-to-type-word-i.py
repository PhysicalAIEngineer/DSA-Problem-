# Brute Force Code & Optimal Code
class Solution:
    def minimumPushes(self, word: str) -> int:
        # there are 8 key available : 2, 3, 4, 5, 6, 7, 8, 9 if the word has 8 or fewer different character each characters can be placed on separate key therefore every characters needs only 1 push
        if len(word) <= 8:
            return len(word)
        # store the total number of pushes requried
        count = 0
        # store how many characters have been assigned to each key mp[key] = number of characters currently assigned to that key
        mp = {}
        # start assigning characters from key 2
        assign = 2
        # process every characters in the word
        for ch in word:
            # there are only 8 key: 2 through 9 after assigning character to key 9 start again from key 2
            if assign > 9:
                assign = 2
            # increase the number of characters assigned to the current key
            mp[assign] = mp.get(assign, 0) + 1
            # push count for a characters depends on its position on the key
            # - 1st character -> 1 push
            # - 2nd character -> 2 pushes
            # - 3rd character -> 3 pushes
            # - 4th character -> 4 pushes
            # mp[assign] the push count needed for the current characters
            count += mp[assign]
            # move the next key
            assign += 1
        # return the total number of pushed
        return count 

# Time Complexity : O(N)
# Space Complexity : O(N)