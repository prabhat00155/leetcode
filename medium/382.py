"""Linked List Random Node
https://leetcode.com/problems/linked-list-random-node
"""


from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.items = []
        ptr = self.head
        while ptr:
            self.items.append(ptr)
            ptr = ptr.next

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.items)-1)
        return self.items[idx].val


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
obj = Solution(head)
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
