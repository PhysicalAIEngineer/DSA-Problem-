# Brute Force Code & Optimal Code
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # store the total number of element in the array 
        n = len(nums)
        # calculate the sum of all elements both subset must together contain all element so their combined sum must equal sum
        SUM = sum(nums)
        # check whether an equal partition is possible 
        # if the total sum is odd, it cannot be divided into two equal interger sum 
        if SUM % 2 != 0:
            return False
        # if the total sum is zero, both subset must have exactly half of the total sum therefore only need to find whether any subset can product the targer sum s
        s = SUM // 2
        # create the memoization tables 
        # create 2D memoization tables with:
        # - n + 1 rows -> number of availables element
        # - s + 1 columns -> possible target sum from 0 to s
        # t[i][j] represents whether can from the target sum j using the first i element of num array 
        # possible values:
        # 1. -1 -> state has not been calculated 
        # 2. 0 -> impossible to from this target sum
        # 3. 1 -> possible to from this target sum
        # intially every state is marked -1 because no recursive state has been evaluated
        t = [[-1] * (s + 1) for _ in range(n + 1)]
        # define the recursive function
        # issubsetsum(n, sum) determines whether can from target sum "sum" using the first "n" element , so have two choices for every element : 1. skip the current element & 2.take current element if its fits and function return true if at least one choice leads to valid subset
        def issubsetSUM(n, target):
            # base case : target sum becomes zero
            # if the remaining target sum is 0, have sucessfully formed the required sum this means can select an empty subset from the remaining element and still achieve the target 
            if target == 0:
                return True
            # base case 2: no element are left
            # if there are no element remaining (n == 0) but the target sum is still greater than 0 cannot from the requried sum therfore return false
            if n == 0:
                return False
            # check whether this recursive state is cached
            # t[n][sum] stores the previosly calculated answer for the current state:
            # n -> number of available element
            # sum -> remaining target sum
            # if the values is not -1 this state has already been calculated instend of performing the same recursive work again directly return the stored result 
            if t[n][target] != -1:
                # convert the stored interger into boolean : 0 -> false & 1 -> true
                return bool(t[n][target])
            # option 1: skip the current element
            # current element is nums[n - 1] if skip it:
            # - remaining target sum does not changes
            # - reduce the number of avaibles element by 1
            # therefore recursively check can from the same target sum using the first n - 1 elements
            skip = issubsetSUM(n - 1, target)
            # option 2: take the current element
            # intially assume that taking the current element will not produce valid subset
            take = False
            # take the current element only if its values is less than or equal to the remaining target sum if nums[n - 1] is greater than sum taking it would exceed the target so this option is not possibles
            if nums[n - 1] <= target:
                # if take the current element:
                # - subtract its values from the target sum
                # - reduce the number of avaibles element by 1
                # remaining target : sum - nums[n - 1] threfore check whether the remaining n - 1 element can from this reduced target sum
                take = issubsetSUM(n - 1, target - nums[n - 1])
            # combine both choices and stores the result
            # valid subset exits if either:
            # -  skipping the current element works 
            # - taking the current element works
            # store the result in memoization tables so that this state does not need to be recalculated
            t[n][target] = int(take or skip)
            # return the stored result as boolean values
            return bool(t[n][target])
        # start the recursive subset sum calculation
        # n = total number of availables element
        # s = required subset sum (half of the total sum)
        # check whether any subset of the entire array can produce the target sum s if true : one subset has sum s and remaining element must also have sum s therefore equal partitioning is possible & if false : no subset can produce the required sum therefore equal paritioning is impossibles
        return issubsetSUM(n, s)

# Time Complexity : O(N)
# Space Complexity : O(N)