"""Operations on Tree
https://leetcode.com/problems/operations-on-tree
"""


class LockingTree:

    def __init__(self, parent: list[int]):
        self.locked = {}
        self.parents = parent
        self.children = [[] for _ in parent]
        for child_node, parent_node in enumerate(parent):
            if parent_node >= 0:
                self.children[parent_node].append(child_node)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num, None) == user:
            del self.locked[num]
            return True
        return False

    def _has_locked_descendant(self, num: int) -> bool:
        if num in self.locked:
            return True
        res = False
        for node in self.children[num]:
            res = res or self._has_locked_descendant(node)
            if res:
                break
        return res

    def _no_locked_ancestors(self, num: int) -> bool:
        if num == -1:
            return True
        if num in self.locked:
            return False
        return self._no_locked_ancestors(self.parents[num])

    def _unlock_descendants(self, num: int):
        for node in self.children[num]:
            if node in self.locked:
                del self.locked[node]
            self._unlock_descendants(node)

    def upgrade(self, num: int, user: int) -> bool:
        if (
            num not in self.locked and self._has_locked_descendant(num)
            and self._no_locked_ancestors(num)
        ):
            self._unlock_descendants(num)
            self.lock(num, user)
            return True

        return False


obj = LockingTree([-1, 0, 0, 1, 1, 2, 2])
print(obj.lock(2, 2))
print(obj.unlock(2, 3))
print(obj.unlock(2, 2))
print(obj.lock(4, 5))
print(obj.upgrade(0, 1))
print(obj.lock(0, 1))
