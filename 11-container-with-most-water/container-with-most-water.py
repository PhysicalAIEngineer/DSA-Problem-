# Optimal Code
class Solution:
    # find the maximum amount of water that can be contained between two lines
    def maxArea(self, height: List[int]) -> int:
        # total number of vertical lines
        n = len(height)
        # intialize two pointer
        # left start as first line
        # right start as end line
        left = 0
        right = n - 1
        # store the maximum water found so 
        maximum_water = 0
        # continue until the two poitner meet
        while left < right:
            # height of the container is limited by the shorter of the two lines
            container_height = min(height[left], height[right])
            # width of the container is the distance between the two pointer
            container_width = right - left
            # calculate the area formed by the current pair of lines
            current_area = container_height * container_width
            # update the maximum area found so far
            maximum_water = max(maximum_water, current_area)
            # move the pointer pointing to the shorter line, since moving the taller line cannot increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # return the maximum amount of water
        return maximum_water

# Time Complexity : O(N)
# Space Complexity : O(N)