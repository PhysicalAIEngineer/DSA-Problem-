# Brute Force Code 
class Solution:
    def smallestChair(self, times: list[list[int]], targetfriend: int) -> int:
        # number of friends
        n = len(times)
        # stroe the departure time of the friend currently sitting on each chair so, index of the list = chair number
        endtimes = [-1] * n
        # store the arrival times of the target friends before sorting the friends because after sorting the original targetfriend index may no longer refer to the same friends
        targetarrivaltime = times[targetfriend][0]
        # sort the all friends by their arrival time so each element is : [arrival_time, departure_time] after sorting friends will be processed in the order they arrive
        times.sort()
        # process every friends in increasing order of arrival times
        for time in times:
            # extract the arrival time of the current friends
            arrival = time[0]
            # extract the depture time sof the current friends
            depature = time[1]
            # try every chair starting from chair 0 
            for i in range(n):
                # check whether chair i is avaliable if endtimes[i] <= arrival then the previous friend has already left when the current friend arrives therefore the chair can be reused
                if endtimes[i] <= arrival:
                    # assign the current friends to this available chair so update the chair depature times to the current friends departure times
                    endtimes[i] = depature
                    # check whehter the current friends is the target friends compare arrival times because all arrival times are distinct
                    if arrival == targetarrivaltime:
                        # return the chair number of immediately
                        return i
                    # current friends has been assigned chair so stop searching for chair and move to the next friends
                    break
        # target friend must always get chair so this line should never be reached
        return - 1

# Time Complexity : O(N^2)
# Space Complexity : O(N)
