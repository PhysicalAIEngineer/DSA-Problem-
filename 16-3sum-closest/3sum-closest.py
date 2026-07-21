# Optimal Code
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # total number of elements
        n = len(nums)
        # sort the array so that two pointer can be used
        nums.sort()
        # store the closest sum found so far initlialized with a large values
        closest_sum = 100000
        # fix the first element of the triplets
        for i in range(n - 2):
            # initialize two pointer
            # left strat after the fixed element
            # right start at the end of array
            left = i + 1
            right = n - 1
            # search for the best pair
            while left < right:
                # calculate the current triplets sum
                current_sum = nums[i] + nums[left] + nums[right]
                # update the closest sum if the curent triplets is closers to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                # if the current sum in greater than the target decrease the sum by moving the right pointer left
                if current_sum > target:
                    right -= 1
                # otherwise increse the sum by moving the left pointer right
                else:
                    left += 1
        # return the closest triplets sum
        return closest_sum 

# Time Complexity : O(Nlog)
# Space Complexity : O(N)  