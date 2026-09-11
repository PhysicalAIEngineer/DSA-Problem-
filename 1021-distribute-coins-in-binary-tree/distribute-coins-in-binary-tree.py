# Brute Force Code & Optimal Code
class Solution:
    def solve(self, root, moves):
        # if the node is None there are no coins or nodes to process
        if root is None:
            return 0
        # calculate the extra coins coming from the left subtree
        l = self.solve(root.left, moves)
        # calculate the extra coins coming from the right subtree
        r = self.solve(root.right, moves)
        # calculate the extra coins that this subtree can send to its parent
        # root.val = coins at current node
        # l        = extra coins from left subtree
        # r        = extra coins from right subtree
        # every node should finally have exactly 1 coin
        total_extra_candies = (l + r + root.val) - 1
        # |l| = number of moves needed between current node and left subtree
        # |r| = number of moves needed between current node and right subtree
        # add both to the total number of moves
        moves[0] += abs(l) + abs(r)
        # Return the extra coins:
        # positive -> extra coins available
        # negative -> coins are needed
        return total_extra_candies
    def distributeCoins(self, root):
        # use a list so that the recursive function can update the same moves value
        moves = [0]
        # if the tree has only one node that node already has the required coin
        if root.left is None and root.right is None:
            return 0
        # start DFS from the root
        self.solve(root, moves)
        # return the minimum number of moves
        return moves[0]

# Time Complexity : O(N)
# Space Complexity : O(N)