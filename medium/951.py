"""Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (
            (self.flipEquiv(root1.left, root2.left)
             and self.flipEquiv(root1.right, root2.right))
            or
            (self.flipEquiv(root1.right, root2.left)
             and self.flipEquiv(root1.left, root2.right))
        )


def test(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    return Solution().flipEquiv(root1, root2)


assert test(
    TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))),
        TreeNode(3, TreeNode(6))),
    TreeNode(
        1, TreeNode(3, None, TreeNode(6)),
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7)))
    ))
assert test(None, None)
assert not test(None, TreeNode(1))
assert not test(
    TreeNode(1, TreeNode(2), TreeNode(3)),
    TreeNode(1, TreeNode(2, TreeNode(3)))
)
