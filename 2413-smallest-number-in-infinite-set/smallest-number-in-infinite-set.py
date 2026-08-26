# Brute Force Code & Optimal Code
class SmallestInfiniteSet:
    def __init__(self):
        # store numbers that have been popped and later added back use a list here to keep the numbers sorted so the smallest added-back number is always at index 0.
        self.st = []
        # smallest number that has never been popped initially, the infinite set contains: 1, 2, 3, 4, 5, ... so the first number we can pop is 1.
        self.currSmallest = 1
    def popSmallest(self):
        # if there are numbers that were previously popped and then added back the smallest one must be returned first.
        if self.st:
            # since st is sorted, the smallest added-back number is at index 0.
            result = self.st[0]
            # remove that number from the added-back list.
            self.st.pop(0)
        else:
            # if no number has been added back return the smallest number that has never been popped before.
            result = self.currSmallest
            # move currSmallest to the next number.
            self.currSmallest += 1
        # return the smallest available number.
        return result
    def addBack(self, num):
        # if num >= currSmallest num has never been popped before,
        # so it is already present in the infinite set.
        if num >= self.currSmallest or num in self.st:
            return
        # add the previously popped number back into the available numbers.
        self.st.append(num)
        # sort the list so that the smallest added-back number stays at index 0.
        self.st.sort()

# Time Complexity : O(Nlog)
# Space Complexity : O(N)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)