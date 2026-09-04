# Brute Force Code & Optimal Code
class Solution: 
    def numRabbits(self, answers): 
        # dictionary to store how many rabbits gave each answer
        # Key   = answer x
        # Value = frequency of rabbits saying x
        mp = {} 
        # count the frequency of each answer
        for x in answers: 
            mp[x] = mp.get(x, 0) + 1 
        # stores the minimum total number of rabbits
        total = 0 
        # process each unique answer and its frequency
        for x, count in mp.items(): 
            # if a rabbit says x, it means there are x other rabbits having the same color so, including the rabbit itself one color group contains x + 1 rabbits.
            groupSize = x + 1 
            # need enough groups to accommodate all rabbits that gave the same answer ceil(count / groupSize) gives the number of groups formula below calculates ceiling division: (count + groupSize - 1) // groupSize
            groups = (count + groupSize - 1) // groupSize 
            # each group contains groupSize rabbits so add the total rabbits from all required groups.
            total += groups * groupSize 
        # return the minimum possible number of rabbits
        return total

# Time Complexity : O(N)
# Space Complexity : O(1)