# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)
        dfs(root)
        return self.result




solution = Solution()
print(solution.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, TreeNode(5)))))


"""
Input: root = [5,4,5,1,1,5]
Output: 2
"""

