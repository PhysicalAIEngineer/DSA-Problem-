class MyCalendar:
    def __init__(self):
        # create an empty list to store all booked events.
        self.events = []
    def book(self, startTime: int, endTime: int) -> bool:
        # go through every event that is already booked need to check whether the new event overlaps with any existing event.
        for start, end in self.events:
            # check whether the new event and the existing event have a non-empty intersection.
            # two intervals overlap when:
            # 1. new event starts before existing event ends startTime < end
            # 2. existing event starts before new event ends start < endTime
            # both conditions must be true for an overlap.
            if startTime < end and start < endTime:
                # an overlap was found therefore, adding this event would create a double booking.
                return False
        # if reach here, the new event did not overlap with any existing event so, add the new event to the calendar.
        self.events.append((startTime, endTime))
        # event was successfully booked.
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)