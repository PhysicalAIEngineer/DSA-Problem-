# Brute Force Code & Optimal Code
class Solution:
    def isNStraightHand(self, hand: List[int], groupsize: int) -> bool:
        # store the total number of cards
        n = len(hand)
        # total number of cards must be divisible by groupsize so that every card can belong to exactly one group
        if n % groupsize != 0:
            return False
        # store the frequency of every card
        mp = {}
        # count how many times each card appears
        for handnumber in hand:
            mp[handnumber] = (mp.get(handnumber, 0) + 1)
        # continue creating groups until all cards have been used
        while mp:
            # always start groups with the smallest card that is still avaiilable 
            current = min(mp)
            # try to create consecutive group
            for i in range(groupsize):
                # calculate the card needed at the current position
                card = current + i
                # if the required card is not avaiilable consecutive group cannot be formed
                if mp.get(card, 0) == 0:
                    return False
                # use one occurence of this card
                mp[card] -= 1
                # if all copies of this card have been used remove if form the frequency map
                if mp[card] < 1:
                    del mp[card]
        # every card was sucessfully used in consecutive groups
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)