# Brute Force Code & Optimal Code
class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int],r: list[int]) -> list[bool]:
        # store whether each query produces an arithmetic sequence
        result = []
        # process every query one by one
        for i in range(len(l)):
            # get the starting and ending index of the current query
            left = l[i]
            right = r[i]
            # extract the elements from nums[left] through nums[right]
            subarray = nums[left:right + 1]
            # sort the subarray so that can easily check whether the elements form an arithmetic sequence.
            subarray.sort()
            # calculate the expected difference using the first two elements.
            difference = subarray[1] - subarray[0]
            # initially assume that the subarray is an arithmetic sequence.
            is_arithmetic = True
            # compare every pair of consecutive elements in the sorted subarray.
            for j in range(1, len(subarray)):
                # calculate the difference between the current element and the previous one.
                current_difference = (subarray[j] - subarray[j - 1])
                # if the difference is not the same as the expected difference the sequence is not arithmetic.
                if current_difference != difference:
                    is_arithmetic = False
                    break
            # store whether this query forms an arithmetic sequence.
            result.append(is_arithmetic)
        # return the answer for all queries
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)