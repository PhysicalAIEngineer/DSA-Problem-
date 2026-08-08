# Brute Force Code & Optimal Code
class Solution:
    def findMinDifference(self, timePoints):
        # number of time points
        n = len(timePoints)
        # create an array to store each time as the total number of minutes from midnight for example: "01:30" -> 1 * 60 + 30 = 90 minutes
        minutes = [0] * n
        # convert every time from "HH:MM" into total minutes.
        for i in range(n):
            # get the current time string
            time = timePoints[i]
            # extract the hour part example: "23:45"
            hourSubstr = time[0:2]
            # extract the minute part
            minSubstr = time[3:5]
            # convert hour and minute strings into integer values.
            hourInt = int(hourSubstr)
            minInt = int(minSubstr)
            # convert the complete time into minutes. example: 23:45
            # = 23 * 60 + 45
            # = 1425 minutes
            minutes[i] = hourInt * 60 + minInt
        # sort all times in increasing order example: [1430, 30, 120]becomes [30, 120, 1430]
        minutes.sort()
        # store the smallest time difference found so far start with infinity because have not calculated any difference yet.
        result = float("inf")
        # check the difference between every pair of neighboring times because the times are sorted, the minimum difference between non-circular times must occur between adjacent elements.
        for i in range(1, n):
            # difference between current time and the previous time.
            difference = minutes[i] - minutes[i - 1]
            # keep the smallest difference.
            result = min(result, difference)
        # check the circular difference time is circular: 23:59 -> 00:00 so also need to compare the last time with the first time by going through midnight minutes remaining from the last time until midnight plus minutes from midnight to the first time.
        # Example:
        # last time  = 23:50 -> 1430
        # first time = 00:10 -> 10
        # difference: (1440 - 1430) + 10 = 20 minutes
        circular_difference = ((24 * 60 - minutes[n - 1]) + minutes[0])
        # return the smaller of:
        # 1. minimum difference between adjacent times
        # 2. circular difference through midnight
        return min(result, circular_difference)

# Time Complexity : O(N)
# Space Complexity : O(N)