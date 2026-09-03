# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # modulo value used in the final answer
        self.M = 10**9 + 7
        # stores the total sum of all nodes in the tree
        self.totalSum = 0
        # stores the maximum product found
        self.maxP = 0
    def findTotalSum(self, root):
        # if the current node is None its subtree sum is 0
        if root is None:
            return 0
        # recursively calculate the sum of the left subtree
        leftSubtreeSum = self.findTotalSum(root.left)
        # recursively calculate the sum of the right subtree
        rightSubtreeSum = self.findTotalSum(root.right)
        # calculate the sum of the current subtree = current node + left subtree + right subtree
        total = root.val + leftSubtreeSum + rightSubtreeSum
        # if cut the edge above this subtree one part has sum 'total' and the other part has sum 'totalSum - total'
        product = (self.totalSum - total) * total
        # update the maximum product found so far
        self.maxP = max(self.maxP, product)
        # return the sum of the current subtree
        return total
    def maxProduct(self, root):
        # if the tree is empty, return 0
        if root is None:
            return 0
        # reset maximum product
        self.maxP = 0
        # first traversal calculate the total sum of the entire tree at this point self.totalSum is 0 so the products calculated during this traversal are ignored
        self.totalSum = self.findTotalSum(root)
        # second traversal now that know the total sum calculate the product for every possible split
        self.findTotalSum(root)
        # return the maximum product modulo 10^9 + 7
        return self.maxP % self.M

# Time Complexity : O(N)
# Space Complexity : O(N)