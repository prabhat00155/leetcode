"""Same Tree
https://leetcode.com/problems/same-tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


def test(p, q):
    print(Solution().isSameTree(p, q))


p = TreeNode(10)
q = None
test(p, q)
q = TreeNode(10)
test(p, q)
q.left = TreeNode(20)
test(p, q)
