# Brute Force Code & Optimal Code
class Solution:
    def isPossible(self, tasks: list[list[int]], mid: int) -> bool:
        # check whether all tasks can be completed when the initial available energy is mid but mid represents the current remaining energy initially, it is equal to the assumed initial energy.
        for task in tasks:
            # extract the actual energy consumed by this task but task[0] represents the energy that will be consumed after successfully completing the task.
            actual = task[0]
            # extract the minimum energy required to start this task but task[1] represents the minimum energy that must be available before beginning this task.
            minimum = task[1]
            # check whether the current remaining energy is sufficient to start the current task if minimum > mid, we do not have enough energy to begin this task therefore, completing all tasks with the assumed initial energy is impossible.
            if minimum > mid:
                # return False immediately because one task cannot be completed.
                return False
            # current task can be completed because the available energy is at least minimum after completing the task, only actual energy is consumed update mid to represent the remaining energy available for the next task.
            mid -= actual
        # if the loop finishes, every task was completed without violating its minimum energy requirement therefore, the assumed initial energy is sufficient.
        return True
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # store the total number of tasks.
        n = len(tasks)
        # initialize the lower boundary of binary search l represents the smallest initial energy currently being considered.
        l = 0
        # Initialize the upper boundary of binary search r represents the largest initial energy currently being considered use 10**9 as the upper search limit.
        r = 10**9
        # store the minimum valid initial energy found so far.
        result = float('inf')
        # sort tasks in descending order based on: minimum - actual
        # - task[1] = minimum energy required before starting.
        # - task[0] = actual energy consumed after completing.
        # A larger difference means the task requires a relatively larger energy reserve compared with the energy it actually consumes such tasks should be performed earlier to minimize the initial energy required reverse=True sorts the tasks from the largest difference to the smallest difference.
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
        # apply binary search to find the minimum initial energy search space is [l, r] continue while l <= r so that every possible candidate in the current search interval is considered.
        while l <= r:
            # calculate the middle value of the current search interval (r - l) // 2 calculates half of the interval length adding l gives the middle position this form avoids calculating l + r directly.
            mid = l + (r - l) // 2
            # check whether all tasks can be completed with mid as the initial energy.
            # isPossible() simulates the tasks in their sorted order.
            # It returns:
            # 1. True  -> mid is sufficient.
            # 2. False -> mid is insufficient.
            if self.isPossible(tasks, mid):
                # current initial energy is sufficient therefore, mid is a valid answer store it as the best answer found so far.
                result = mid
                # try to find an even smaller valid initial energy since mid is already sufficient, any value greater than mid is unnecessary to investigate move the upper boundary to mid - 1.
                r = mid - 1
            else:
                # current initial energy is insufficient therefore, every value smaller than mid
                # is also insufficient increase the lower boundary to mid + 1 and search for a larger initial energy.
                l = mid + 1
        # return the smallest initial energy that successfully completes every task.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)