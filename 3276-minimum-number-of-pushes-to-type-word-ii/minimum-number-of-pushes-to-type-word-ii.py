# Brute Force Code & Optimal Code
class Solution:
    # sort characters in decreasing order of frequency characters that appear more frequently should get positions requiring fewer pushes.
    def sortFunc(self, word):
        # store the frequency of every character.
        mp = {}
        # count how many times each character appears.
        for ch in word:
            mp[ch] = mp.get(ch, 0) + 1
        # sort all characters by their frequency from highest to lowest.
        word = sorted(word, key=lambda ch: mp[ch], reverse=True)
        # return the characters sorted by decreasing frequency.
        return word
    def minimumPushes(self, word):
        # there are 8 available keys: 2, 3, 4, 5, 6, 7, 8, 9 if there are 8 or fewer different characters every character can be assigned to its own key and needs only 1 push.
        if len(word) <= 8:
            return len(word)
        # sort characters by decreasing frequency this ensures that characters appearing more often are assigned to positions requiring fewer pushes.
        word = self.sortFunc(word)
        # myMap[key] stores the different characters assigned to that key.
        myMap = {}
        # mp[character] = (key, position)
        # Example:
        # mp['a'] = (2, 1)
        # mp['b'] = (2, 2)
        # this tells us:
        # - which key the character is assigned to
        # - how many pushes are needed for that character
        mp = {}
        # store the total number of pushes.
        result = 0
        # start assigning new characters from key 2.
        assign = 2
        # process characters in decreasing frequency order.
        for ch in word:
            # there are only 8 keys: 2 to 9 after key 9, start again from key 2.
            if assign > 9:
                assign = 2
            # assign the character only the first time encounter it.
            if ch not in mp:
                # create an empty set for the key if this key has not been used yet.
                if assign not in myMap:
                    myMap[assign] = set()
                # assign the new character to this key.
                myMap[assign].add(ch)
                # number of characters currently assigned to this key determines the number of pushes.
                # first character  -> 1 push
                # second character -> 2 pushes
                # third character  -> 3 pushes
                position = len(myMap[assign])
                # atore the key and push count for this character.
                mp[ch] = (assign, position)
                # add the push count for this occurrence.
                result += position
                # move to the next key for the next new character.
                assign += 1
            else:
                # character has already been assigned to a key every occurrence of the same character requires the same number of pushes.
                result += mp[ch][1]
        # return the minimum total number of pushes.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)