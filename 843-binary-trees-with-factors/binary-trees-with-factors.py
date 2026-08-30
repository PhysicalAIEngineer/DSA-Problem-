# Brute Force Code & Optimal Code 
class Solution:
    def numFactoredBinaryTrees(self, arr):
        # modulo value used because the answer can become very large.
        MOD = 10**9 + 7
        # number of elements in the array.
        n = len(arr)
        # sort the array this allows us to process smaller values before larger values.
        arr.sort()
        # dp[x] = number of different binary trees that can be formed with x as the root.
        mp = {}
        # single element by itself forms one valid binary tree.
        mp[arr[0]] = 1
        # process every value starting from the second element.
        for i in range(1, n):
            # at minimum, arr[i] can form a single-node tree.
            count = 1
            # try every previously processed value as the left child.
            for j in range(i):
                # choose arr[j] as the left child.
                left = arr[j]
                # for arr[i] to be the root need: left * right = arr[i] therefore: right = arr[i] / left check that arr[i] is divisible by left and that the right child exists.
                if (arr[i] % left == 0 and (arr[i] // left) in mp):
                    # number of ways to build the left subtree.
                    leftWays = mp[left]
                    # number of ways to build the right subtree.
                    rightWays = mp[arr[i] // left]
                    # every left subtree can be combined with every right subtree therefore: total combinations = leftWays * rightWays
                    count += leftWays * rightWays
            # store the number of binary trees having arr[i] as the root.
            mp[arr[i]] = count
        # store the total number of valid trees.
        result = 0
        # add the number of trees for every possible root value.
        for value in mp:
            # apply modulo to keep the number small.
            result = (result + mp[value]) % MOD
        # return the total number of factored binary trees.
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)