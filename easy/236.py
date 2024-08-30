"""Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        lca = None

        def find(node):
            nonlocal lca
            if not node or lca:
                return 0
            return_val = (find(node.left) + find(node.right)
                          + int(node == p) + int(node == q))
            if return_val == 2:
                lca = node
                return 0
            return return_val

        find(root)
        return lca


def test(root, p, q):
    print(Solution().lowestCommonAncestor(root, p, q).val)


root = TreeNode(
    3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8)))
p, q = root.left, root.right
test(root, p, q)
p, q = root.left, root.left.right.right
test(root, p, q)
