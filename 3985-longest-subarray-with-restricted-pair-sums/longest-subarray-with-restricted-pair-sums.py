class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        v = 500
        freq = [0] * (v + 1)
        pairs = [0] * (v + 1)
        left = 0
        bad = 0
        answer = 0
        for right, x in enumerate(nums):
            bad += pairs[x]
            limit = v - x
            for a in range(1, limit + 1):
                cnt = freq[a]
                if cnt:
                    s = x + a
                    bad += cnt * freq[s]
                    pairs[s] += cnt
            freq[x] += 1
            while bad > 0:
                y = nums[left]
                freq[y] -= 1
                bad -= pairs[y]
                limit = v - y
                for a in range(1, limit + 1):
                    cnt = freq[a]
                    if cnt:
                        s = y + a
                        bad -= cnt * freq[s]
                        pairs[s] -= cnt
                left += 1
            answer = max(answer, right - left + 1)
        return answer 