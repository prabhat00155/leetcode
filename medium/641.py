"""Design Circular Deque
https://leetcode.com/problems/design-circular-deque
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.size = k
        self.first = -1
        self.last = -1

    def insertFront(self, value: int) -> bool:
        if self.first == -1:
            self.first = 1
            self.last = 0
        if self.q[(self.first - 1) % self.size] is not None:
            return False
        self.first = (self.first - 1) % self.size
        self.q[self.first] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.last == -1:
            self.first = 0
        if self.q[(self.last + 1) % self.size] is not None:
            return False
        self.last = (self.last + 1) % self.size
        self.q[self.last] = value
        return True

    def deleteFront(self) -> bool:
        if self.first == -1:
            return False
        self.q[self.first] = None
        self.first = (self.first + 1) % self.size
        if self.q[self.first] is None:
            self.first = -1
            self.last = -1
        return True

    def deleteLast(self) -> bool:
        if self.last == -1:
            return False
        self.q[self.last] = None
        self.last = (self.last - 1) % self.size
        if self.q[self.last] is None:
            self.last = -1
            self.first = -1
        return True

    def getFront(self) -> int:
        return -1 if self.first == -1 else self.q[self.first]

    def getRear(self) -> int:
        return -1 if self.last == -1 else self.q[self.last]

    def isEmpty(self) -> bool:
        return self.last == -1

    def isFull(self) -> bool:
        return self.first == (self.last + 1) % self.size


obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())
