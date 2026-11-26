# Brute Force Code & Optimal Code
class Solution:
    MOD = 10**9 + 7
    def findPower(self, a: int, base: int) -> int:
        if base == 0:
            return 1
        half = self.findPower(a, base // 2)
        result = (half * half) % self.MOD
        if base % 2 == 1:
            result = (result * a) % self.MOD
        return result
    def check(self, nums: list[int], size: int, base: int) -> bool:
        n = len(nums)
        hash_value = 0
        mp = {}
        p = self.findPower(base, size - 1)
        i = 0
        j = 0
        while j < n:
            hash_value = (hash_value * base + nums[j]) % self.MOD
            if j - i + 1 < size:
                j += 1
            else:
                mp[hash_value] = mp.get(hash_value, 0) + 1
                hash_value = (hash_value - (p * nums[i]) % self.MOD + self.MOD) % self.MOD
                i += 1
                j += 1
        for frequency in mp.values():
            if frequency == 1:
                return True
        return False
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base = max(nums) + 1
        l = 1
        r = n
        result = n
        while l <= r:
            mid = l + (r - l) // 2
            if self.check(nums, mid, base):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)