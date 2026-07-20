# Optimal Code
class Solution:
    def find_first_position(self, nums: list[int], target: int): 
        # intialize the binary search boundaries
        left = 0
        right = len(nums) - 1
        # store the first occurence of the target intialize with -1 (target not found)
        result = -1
        # perform binary search
        while left <= right:
            # find the middle index
            mid = left + (right - left) // 2
            # target found
            if nums[mid] == target:
                # store the current index as a possible numbers
                result = mid
                # continue searching on the left side to find an earlier occurences
                right = mid - 1
            # target lies in the left half
            elif nums[mid] > target:
                right = mid - 1
            # target lies in the right half
            else:
                left = mid + 1
        # return the first occurence index
        return result 
    # find the last occurence of the target
    def find_last_position(self, nums: list[int], target: int):
        # intialize the binary search boundaries
        left = 0
        right = len(nums) - 1
        # storet the last occurence of the target initlaize with -1 (target not found)
        result = -1
        # perform binary search
        while left <= right:
            # find the middle index
            mid = left + (right - left) // 2
            # target found
            if nums[mid] == target:
                # store the current index as a possible numbers
                result = mid
                # continue searching on the right side to find a later occurence
                left = mid + 1
            # target lies in the left half
            elif nums[mid] > target:
                right = mid - 1
            # target lies in the right half
            else:
                left = mid + 1
        # return the last occurence index
        return result
    # return the first and last occurences of the target  
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the first occurence of the target
        first = self.find_first_position(nums, target)
        # find the last occurence of the target
        last = self.find_last_position(nums, target)
        # return the both indices if the target does not exists both values will be -1
        return [first, last]

# Time Complexity : O(Nlog)
# Space Complexity : O(1)