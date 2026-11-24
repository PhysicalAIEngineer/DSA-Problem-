class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        answer = (nums[0] >= nums[1]) + (nums[-1] >= nums[-2])
        for i in range(1, n - 1):
            answer += 2 * nums[i] >= nums[i - 1] + nums[i + 1]
        return answer 