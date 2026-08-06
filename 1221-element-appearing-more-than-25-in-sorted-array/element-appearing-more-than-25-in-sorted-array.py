# Brute Force Code & Optimal Code
class Solution:
    def firstOccur(self, target: int, left: int, right: int, arr: list[int]) -> int:
        # store the first occurrence of target initially, target has not been found.
        result = -1
        # continue binary search while the search range is valid.
        while left <= right:
            # find the middle index.
            mid = left + (right - left) // 2
            # if found the target
            if arr[mid] == target:
                # store this index as a possible first occurrence.
                result = mid
                # there may be another occurrence of target further to the left so continue searching in the left half.
                right = mid - 1
            # if the middle value is smaller than target
            elif arr[mid] < target:
                # target can only exist on the right side.
                left = mid + 1
            # if the middle value is greater than target
            else:
                # target can only exist on the left side.
                right = mid - 1
        # return the first occurrence returns -1 if target was not found.
        return result
    def lastOccur(self, target: int, left: int, right: int, arr: list[int]) -> int:
        # store the last occurrence of target. initially, target has not been found.
        result = -1
        # continue binary search while the search range is valid.
        while left <= right:
            # find the middle index.
            mid = left + (right - left) // 2
            # if found the target
            if arr[mid] == target:
                # store this index as a possible last occurrence.
                result = mid
                # there may be another occurrence of target further to the right so continue searching in the right half.
                left = mid + 1
            # if the middle value is smaller than target
            elif arr[mid] < target:
                # target can only exist on the right side.
                left = mid + 1
            # if the middle value is greater than target
            else:
                # target can only exist on the left side.
                right = mid - 1
        # return the last occurrence  returns -1 if target was not found.
        return result
    def findSpecialInteger(self, arr: list[int]) -> int:
        # number of elements in the sorted array
        n = len(arr)
        # special element must occur strictly more than n / 4 times n // 4 gives the integer part of n/4.
        freq = n // 4
        # choose possible candidates since arr is sorted, an element that occurs more than 25% of the time must cross one of these positions: n/4, n/2, or 3n/4 therefore, we only need to check these three elements.
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        # check each possible candidate
        for candidate in candidates:
            # find the first occurrence of the candidate
            left = self.firstOccur(candidate, 0, n - 1,arr)
            # find the last occurrence of the candidate
            right = self.lastOccur(candidate, 0, n - 1, arr)
            # calculate how many times the candidate occurs.
            count = right - left + 1
            # check whether the candidate occurs more than 25% of the array.
            if count > freq:
                return candidate
        # no valid special integer was found.
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N)