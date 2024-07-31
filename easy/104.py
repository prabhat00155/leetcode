"""Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test(root):
    print(Solution().maxDepth(root))


test(TreeNode(3, TreeNode(9),
              TreeNode(20, TreeNode(15), TreeNode(7))))
test(TreeNode(1, None, TreeNode(2)))
