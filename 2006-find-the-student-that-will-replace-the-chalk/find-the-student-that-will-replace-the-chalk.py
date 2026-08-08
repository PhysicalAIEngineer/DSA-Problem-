# Optimal Code
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # store the number of students
        n = len(chalk)
        # calculate the total amount of chalk required for all students to complete one full round
        totalchalksum = 0
        for chalkreq in chalk:
            # add the current students chalk requirement to the total for one complete round
            totalchalksum += chalkreq
        # remove as many complete round as possible 
        remainchalk = k % totalchalksum
        # start from students 0 need to process the remaining chalk because all complete round have already been removed using the modulo operation
        for i in range(n):
            # check whether the current students has enough remaining chalk if remainchalk is smaller than chalk[i] this students cannot get the required amount therefore this students is the answer
            if remainchalk < chalk[i]:
                return i
            # current students has enough chalk give this students the required chalk and subtract from the remaining amount
            remainchalk -= chalk[i]
        # this line is normally unrechable because the problem gurantees that some studnets will not have enough chalk
        return -1

# Time Complexity : O(N)
# Space Complexity : O(1)
