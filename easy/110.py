"""Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height_diff(root):
            if not root:
                return 0
            left = 1 + height_diff(root.left)
            right = 1 + height_diff(root.right)
            if abs(left-right) > 1:
                nonlocal balanced
                balanced = False
            return max(left, right)

        height_diff(root)
        return balanced


def test(root):
    print(Solution().isBalanced(root))


test(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
test(TreeNode(
    1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
    TreeNode(2)))
test(None)
