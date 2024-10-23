"""Cousins in Binary Tree II
https://leetcode.com/problems/cousins-in-binary-tree-ii
"""


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque()
        q.append((root, None))
        while q:
            size = len(q)
            level_sum = 0
            mapper = {}
            for i in range(size):
                node, parent = q.popleft()
                if parent:
                    mapper[parent] = mapper.get(parent, 0) + node.val
                else:
                    node.val = 0
                level_sum += node.val
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            for node, total in mapper.items():
                if node.left:
                    node.left.val = level_sum - total
                if node.right:
                    node.right.val = level_sum - total
        return root


def test(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().replaceValueInTree(root)


def dfs(node):
    if node:
        dfs(node.left)
        print(node.val, end=' ')
        dfs(node.right)


root = TreeNode(
    5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, None, TreeNode(7)))
print('Test case 1:\nOriginal Tree:')
dfs(root)
root = test(root)
print('\nResulting Tree:')
dfs(root)
print()

root = TreeNode(3, TreeNode(1), TreeNode(2))
print('\nTest case 2:\nOriginal Tree:')
dfs(root)
root = test(root)
print('\nResulting Tree:')
dfs(root)
print()
