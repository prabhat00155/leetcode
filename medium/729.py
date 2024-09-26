"""My Calendar I
https://leetcode.com/problems/my-calendar-i
"""


class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, start: int, end: int):
        if not self.root:
            self.root = Node(start, end)
            return True
        node = self.root
        while True:
            if (
                node.start <= start < node.end or node.start < end < node.end
                or start <= node.start < end or start < node.end < end
            ):
                return False
            if end <= node.start:
                if not node.left:
                    node.left = Node(start, end)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = Node(start, end)
                    break
                node = node.right
        return True


class MyCalendar:

    def __init__(self):
        self.bst = BST()

    def book(self, start: int, end: int) -> bool:
        return self.bst.insert(start, end)


def test(arr):
    obj = MyCalendar()
    res = []
    for start, end in arr:
        res.append(obj.book(start, end))
    print(res)


test([[10, 20], [15, 25], [20, 30]])
test([
    [47, 50], [33, 41], [39, 45], [33, 42], [25, 32],
    [26, 35], [19, 25], [3, 8], [8, 13], [18, 27],
])
test([[37, 50], [33, 50], [4, 17], [35, 48], [8, 25]])
