"""Linked List in Binary Tree
https://leetcode.com/problems/linked-list-in-binary-tree
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        def scan(t_node, l_node):
            if not l_node:
                return True
            if not t_node:
                return False
            if t_node.val == l_node.val:
                return scan(t_node.left, l_node.next) or scan(
                    t_node.right, l_node.next)
            return False

        def traverse(t_node):
            if not t_node:
                return False
            return scan(t_node, head) or traverse(t_node.left) or traverse(
                t_node.right)

        return traverse(root)


def test(head: Optional[ListNode], root: Optional[TreeNode]):
    print(Solution().isSubPath(head, root))


test(
    ListNode(4, ListNode(2, ListNode(8))),
    TreeNode(
        1,
        TreeNode(4, right=TreeNode(2, TreeNode(1))),
        TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1),
                                                      TreeNode(3))))))
test(
    ListNode(1, ListNode(4, ListNode(2, ListNode(6)))),
    TreeNode(
        1,
        TreeNode(4, right=TreeNode(2, TreeNode(1))),
        TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1),
                                                      TreeNode(3))))))
test(
    ListNode(1, ListNode(4, ListNode(2, ListNode(6, ListNode(8))))),
    TreeNode(
        1,
        TreeNode(4, right=TreeNode(2, TreeNode(1))),
        TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1),
                                                      TreeNode(3))))))
test(ListNode(2, ListNode(2, ListNode(1))),
     TreeNode(2, right=TreeNode(2, right=TreeNode(2, TreeNode(1)))))
