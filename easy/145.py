"""Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        output = []

        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                nonlocal output
                output.append(root.val)

        post_order(root)
        return output


def test(root):
    print(Solution().postorderTraversal(root))


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
test(root)
