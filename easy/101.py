"""Symmetric Tree
https://leetcode.com/problems/symmetric-tree
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        while q:
            item_count = len(q)
            level = []
            for _ in range(item_count):
                node = q.popleft()
                if not node:
                    level.append(None)
                else:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level != level[::-1]:
                return False
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(Solution().isSymmetric(root))
