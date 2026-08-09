# Brute Force Code & Optimal Code
class MyCalendarTwo:
    def __init__(self):
        # store all regions that are already covered by two events this region cannot overlap with a new event because that would create a triple booking.
        self.doubleOverlappedRegion = []
        # store every event that has been successfully booked.
        self.overallBookings = []
    def checkOverlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        # check whether two intervals overlap the intervals overlap when: max(start1, start2) < min(end1, end2)
        return max(start1, start2) < min(end1, end2)
    def findOverlappedRegion(self, start1: int, end1: int,start2: int, end2: int) -> tuple:
        # find the exact region where the two intervals overlap start of the overlap is the later of the two start times end of the overlap is the earlier of the two end times.
        return (max(start1, start2), min(end1, end2))
    def book(self, start: int, end: int) -> bool:
        # check for triple booking doubleOverlappedRegion contains regions where two events are already booked if the new event overlaps with any of these
        # regions, that part would be covered by
        # three events triple booking is not allowed.
        for region in self.doubleOverlappedRegion:
            # check whether the new event overlaps with an already double-booked region.
            if self.checkOverlap(region[0], region[1], start, end):
                # triple booking would occur so reject the new event.
                return False
        # find new double-booked region now check the new event against every successfully booked even any overlap between them means that those time periods will now be covered by two events.
        for booking in self.overallBookings:
            # check whether the new event overlaps with the current existing booking.
            if self.checkOverlap(booking[0], booking[1],start,end):
                # find the exact region where the existing booking and the new booking overlap.
                overlap = self.findOverlappedRegion(booking[0],booking[1],start,end)
                # store this region as a double-booked region in the future, a new event cannot overlap with this region because that would create a triple booking.
                self.doubleOverlappedRegion.append(overlap)
        # store the new booking new event did not create a triple booking so it is safe to add it to all bookings.
        self.overallBookings.append((start, end))
        # booking was successfully added.
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)