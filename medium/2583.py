"""Kth Largest Sum in a Binary Tree
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree
"""


from collections import deque
from typing import Optional
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        min_heap = []

        q.append(root)
        while q:
            size = len(q)
            cur_sum = 0
            for i in range(size):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(min_heap) < k:
                heapq.heappush(min_heap, cur_sum)
            else:
                heapq.heappushpop(min_heap, cur_sum)
        return min_heap[0] if len(min_heap) == k else -1


def test(root: Optional[TreeNode], k: int) -> int:
    return Solution().kthLargestLevelSum(root, k)


assert test(TreeNode(
    5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)),
    TreeNode(9, TreeNode(3), TreeNode(7))), 2) == 13
assert test(TreeNode(1, TreeNode(2, TreeNode(3))), 1) == 3
