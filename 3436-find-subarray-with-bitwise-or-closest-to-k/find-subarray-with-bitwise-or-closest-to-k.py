class Node:
    def __init__(self, arr: List[int], l: int, r: int):
        self.l = l
        self.r = r
        if l == r: 
            self.value = arr[l]
        else:
            mid = (l + r) // 2
            self.left = Node(arr, l, mid)
            self.right = Node(arr, mid + 1, r)
            self.value = self.left.value | self.right.value

    def find(self, l: int, r: int) -> int:
        if self.r < l or self.l > r: return 0
        elif l <= self.l and self.r <= r: return self.value
        else:
            return self.left.find(l, r) | self.right.find(l, r)

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # First idea O(N ^ 2)
        # BS for each l, find an r st [l, r] is closest to k
        # closest_to == greaterThanOrEqual + lesserOne

# sliding window ------------------------------------------------------------------------------
        # Why not simple sliding window, because we can't revert OR. Although we can use segtree to get to a O(nlog2n) solution.
        N = len(nums)
        root = Node(nums, 0, N - 1)
        ans = float('inf')
        j = 0
        for i in range(N):
            j = max(i, j)
            while j < N and root.find(i, j) < k:
                j += 1
            
            if i == j:
                ans = min(ans, abs(k - nums[i]))
            else:
                closest = root.find(i, j - 1)
                ans = min(ans, abs(k - closest))
                if j < N:
                    ans = min(ans, abs(k - (closest | nums[j])))
        return ans 
                
# old -----------------------------------------------------------------
        N = len(nums)
        root = Node(nums, 0, N - 1)
        def findSmallestGreaterThanOrEqual(startIdx: int, target: int) -> int:
            # invariant smallest greater than or equal to target will be in range [l, r]
            if root.find(startIdx, N - 1) < target: return N - 1
            l, r = startIdx, N - 1
            while l < r:
                mid = l + (r - l) // 2
                val = root.find(startIdx, mid)
                if val == target: return mid
                elif val < target: l = mid + 1
                else: r = mid
            return r
            
        ans = float('inf')
        for l in range(N):
            idx = findSmallestGreaterThanOrEqual(l, k)

            if idx - 1 >= l:
                closest = root.find(l, idx - 1)
                ans = min(ans, abs(k - closest))
                ans = min(ans, abs(k - (closest | nums[idx])))
            else:
                closest = root.find(l, idx)
                ans = min(ans, abs(k - closest))
        return ans 