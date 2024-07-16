"""Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        ptr = self
        while ptr:
            nodes.append(f'{ptr.val}')
            ptr = ptr.next
        return '->'.join(nodes)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test(head):
    print(Solution().middleNode(head))


head = ListNode(1)
test(head)
head.next = ListNode(2)
test(head)
head.next.next = ListNode(3)
test(head)
head.next.next.next = ListNode(4)
test(head)
head.next.next.next.next = ListNode(5)
test(head)
head.next.next.next.next.next = ListNode(6)
test(head)
