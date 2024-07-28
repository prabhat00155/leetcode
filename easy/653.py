"""Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elements = set()

        def find(root):
            if not root:
                return False
            if root.val in elements:
                return True
            elements.add(k-root.val)
            return find(root.left) or find(root.right)

        return find(root)


def test(root, k):
    print(Solution().findTarget(root, k))


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
test(root, 9)
