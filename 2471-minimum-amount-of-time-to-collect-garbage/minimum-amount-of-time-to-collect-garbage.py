# Brute Force Code & Optimal Code
class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        # number of houses
        n = len(garbage)
        # store the last house where each type of garbage appears.
        # G -> last house containing glass
        # M -> last house containing metal
        # P -> last house containing paper
        G = 0
        M = 0
        P = 0
        # total time required to collect all garbage
        total = 0
        # visit every house
        for i in range(n):
            # check every piece of garbage present at the current house
            for ch in garbage[i]:
                # picking up one piece of garbage takes exactly 1 minute.
                total += 1
                # remember the latest house containing this type of garbage.
                if ch == 'M':
                    M = i
                elif ch == 'P':
                    P = i
                else:
                    # remaining garbage type is Glass
                    G = i
        # convert travel[] into prefix sums before: travel[i] = time to travel from house i to house i + 1 and  after: travel[i] = total travel time from house 0  to house i + 1
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        # metal truck only needs to travel until the last house containing metal travel[M - 1] gives the total travel time from house 0 to house M.
        if M > 0:
            total += travel[M - 1]
        # paper truck only needs to travel until the last house containing Paper.
        if P > 0:
            total += travel[P - 1]
        # glass truck only needs to travel until the last house containing Glass.
        if G > 0:
            total += travel[G - 1]
        # total time = garbage collection time + required travel time
        return total

# Time Complexity : O(N)
# Space Complexity : O(1)