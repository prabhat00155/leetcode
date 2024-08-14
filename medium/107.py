"""Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii
"""


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return
        q = deque()
        q.append(root)
        output = deque()
        while q:
            cur_level = len(q)
            cur_output = []
            for i in range(cur_level):
                node = q.popleft()
                cur_output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.appendleft(cur_output)
        return list(output)


def test(root):
    print(Solution().levelOrderBottom(root))


test(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
test(TreeNode(1))
test(None)
