# Optimal Code
class Solution:
    # divide all people into groups such that every person group has exactly the size specified by groupSizes[person].
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        # total number of people
        n = len(groupSizes)
        # create buckets for each possible group size mp[x] stores the people who need a group of size x.
        mp = [[] for _ in range(n + 1)]
        # store the final list of groups
        result = []
        # traverse every person
        for i in range(n):
            # required group size for the current person
            group_size = groupSizes[i]
            # put the person's index into the bucket corresponding to their required group size.
            mp[group_size].append(i)
            # check whether we have enough people to form one complete group.
            if len(mp[group_size]) == group_size:
                # add the complete group to the result.
                result.append(mp[group_size])
                # clear the bucket more people may require the same group size, so  start collecting the next group.
                mp[group_size] = []
        # return all valid groups
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)