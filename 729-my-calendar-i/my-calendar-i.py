from bisect import bisect_left
class MyCalendar:
    def __init__(self):
        # create a list to store all booked events each event is stored as: (start, end)
        self.st = []
    def book(self, start: int, end: int) -> bool:
        # find the first event whose start time is greater than or equal to the new event's start time.
        index = bisect_left(self.st, (start, end))
        # check if the current event overlaps with the next event if the next event starts before the new event ends then the two events overlap.
        if index < len(self.st) and self.st[index][0] < end:
            return False
        # check if the current event overlaps with the previous event.
        if index > 0:
            # get the previous event.
            previous_event = self.st[index - 1]
            # if the new event starts before the previous event ends, then the two events overlap.
            if start < previous_event[1]:
                return False
        # no overlap was found insert the new event at the correct sorted position.
        self.st.insert(index, (start, end))
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)