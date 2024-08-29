"""Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(
            root.right, low, high) + self.rangeSumBST(root.left, low, high)


def test(root: Optional[TreeNode], low: int, high: int):
    print(Solution().rangeSumBST(root, low, high))


test(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)),
              TreeNode(15, None, TreeNode(18))), 7, 15)
