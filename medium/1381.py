"""Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.max_size:
            self.stk.append(x)

    def pop(self) -> int:
        return self.stk.pop() if len(self.stk) > 0 else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == len(self.stk):
                break
            self.stk[i] += val


obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
