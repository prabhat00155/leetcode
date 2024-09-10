"""Insert Greatest Common Divisors in Linked List
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            while a % b != 0:
                a, b = b, a % b
            return b

        p, q = head, head.next
        while q:
            new_node = ListNode(gcd(p.val, q.val), q)
            p.next = new_node
            p = q
            q = q.next
        return head


def test(head: Optional[ListNode]):
    print_list(Solution().insertGreatestCommonDivisors(head))


test(ListNode(18, ListNode(6, ListNode(10, ListNode(3)))))
test(ListNode(7))
