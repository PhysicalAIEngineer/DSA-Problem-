# Brute Force Code & Optimal Code
class Solution:
    def getSortedStr(self, n: int) -> str:
        # convert the given integer into a string this allows us to access and sort its individual digits.
        s = str(n)
        # sort all digits of the string in ascending order.
        s = ''.join(sorted(s))
        # return the sorted digit string.
        return s
    def reorderedPowerOf2(self, n: int) -> bool:
        # sorted digit string of the given number this represents the digit composition of n independent of the original order of its digits
        s = self.getSortedStr(n)
        # check all possible powers of 2 from 2^0 through 2^29.
        for p in range(30):
            # calculate the current power of 2 the left shift operator (<<) shifts the binary representation of 1 to the left by p positions.
            power = 1 << p
            # sort the digits of the current power of 2 and compare them with the sorted digits of n if both sorted strings are equal, the two numbers contain exactly the same digits with the same frequencies therefore, the digits of n can be rearranged to form this power of 2.
            if s == self.getSortedStr(power):
                # matching power of 2 has been found return True immediately because no further powers need to be checked.
                return True
        # if the loop finishes without finding a matching power none of the checked powers of 2 can be formed by rearranging the digits of n therefore, return False.
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)