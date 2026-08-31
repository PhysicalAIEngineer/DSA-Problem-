// Brute Force Code & Optimal Code
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupsize) {
        // store the total number of cards.
        int n = hand.size();
        // total number of cards must be divisible by groupsize so that every card can belong to exactly one group.
        if (n % groupsize != 0) {
            return false;
        }
        // store the frequency of every card.
        map<int, int> mp;
        // count how many times each card appears.
        for (int handnumber : hand) {
            mp[handnumber]++;
        }
        // continue creating groups until all cards have been used.
        while (!mp.empty()) {
            // always start the group with the smallest card that is still available.
            int current = mp.begin()->first;
            // try to create a consecutive group.
            for (int i = 0; i < groupsize; i++) {
                // calculate the card needed at the current position.
                int card = current + i;
                // if the required card is not available a consecutive group cannot be formed.
                if (mp.find(card) == mp.end()) {
                    return false;
                }
                // use one occurrence of this card.
                mp[card]--;
                // if all copies of this card have been used remove it from the frequency map.
                if (mp[card] < 1) {
                    mp.erase(card);
                }
            }
        }
        // every card was successfully used in consecutive groups.
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)