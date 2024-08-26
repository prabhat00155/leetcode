"""N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return None
        output = []
        for child in root.children:
            ret = self.postorder(child)
            if ret:
                output.extend(ret)
        output.append(root.val)
        return output


def test(root):
    print(Solution().postorder(root))


test(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]))
