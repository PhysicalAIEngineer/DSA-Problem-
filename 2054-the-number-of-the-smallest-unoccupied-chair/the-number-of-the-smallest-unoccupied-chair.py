# Optimal Code
class Solution:
    def smallestChair(self, times: list[list[int]], targetfriend: int) -> int:
        # number of friends
        n = len(times)
        # min heap storing occupied chairs so each element is : (depature_time, chair_number)
        occupied = []
        # min heap storing chair numbers that are currently available smllest chair number will always be at the top
        free = []
        # store the arrival time of the target friends before sorting the input 
        targetfriendarrial = times[targetfriend][0]
        # sort al friends by their arrival time so, each friend is represented as : [arrival_time, depature_time]
        times.sort()
        # new chair that has never been assigned before 
        chairno = 0
        # process every friend in incresing order of arrival time
        for i in range(n):
            # arrival time of the current friends
            arrival = times[i][0]
            # depature time of the current friends
            depat = times[i][1]
            # free all chair whose occupants have left top of the occupied heap contain the friends whose leaves earliest if their depature time <= arrival their chair is avalible for the current friends continue until every chair whose occupant has already left is moved into the free heap
            while occupied and occupied[0][0] <= arrival:
                # get the chair number of the friends whose leaves earliest
                chair = occupied[0][1]
                # add this chair to the free chair heap because free is min heap the smallest available chair will be selected later
                heapq.heappush(free, chair)
                # remove this departed friends from the occupied heap
                heapq.heappop(occupied)
            # case 1: no previously used chair is free 
            if not free:
                # assign the next completely new chair to the current friends
                heapq.heappush(occupied, (depat, chairno))
                # check whether the current friends is the target friends
                if arrival == targetfriendarrial:
                    # return the chair assinged to the target friends
                    return chairno
                # current new chair number has now beeen used so the next new chair will have the next number
                chairno += 1
            # case 2: at least one chair is avalilables
            else:
                # smallest available chair is the top of the free min heap
                leastchairavaliable = free[0]
                # remove the smallest chair from the free heap because are going tot assign the current friends
                heapq.heappop(free)
                # check whether the current friends is the target friends
                if arrival == targetfriendarrial:
                    # return the smallest available chair numbers
                    return leastchairavaliable
                # chiar is occupied again by the current friends
                heapq.heappush(occupied, (depat, leastchairavaliable))
        # target friends must always receive chair 
        return -1 

# Time Complexity : O(N)
# Space Complexity : O(N)
        