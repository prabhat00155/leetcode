"""Find Elements in a Contaminated Binary Tree
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        def recover(node, value):
            if not node:
                return
            node.val = value
            recover(node.left, 2*value+1)
            recover(node.right, 2*value+2)

        recover(self.root, 0)

    def find(self, target: int) -> bool:
        def find_all(node):
            if not node:
                return False
            if node.val == target:
                return True
            return find_all(node.left) or find_all(node.right)

        return find_all(self.root)


root = TreeNode(-1)
root.right = TreeNode(-1)
obj = FindElements(root)
print(obj.find(1))
print(obj.find(2))
