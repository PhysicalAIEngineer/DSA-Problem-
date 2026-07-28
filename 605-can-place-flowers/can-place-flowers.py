# Brute Force Code & Optimal Code
class Solution:
    # check whether n new flowers can be planted without placing flowers in adjacent plots
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # total number of plots
        length = len(flowerbed)
        # if no flowers need to be planted the answer is always True
        if n == 0:
            return True
        # traverse every plot
        for i in range(length):
            # only consider empty plots
            if flowerbed[i] == 0:
                # check whether the left plot is empty or if this is the first plot
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                # check whether the right plot is empty, or if this is the last plot
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                # plant a flower if both neighboring plots are empty
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    # if all required flowers have been planted return True
                    if n == 0:
                        return True
        # not enough valid positions were available
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)