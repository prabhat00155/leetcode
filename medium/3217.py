"""Delete Nodes From Linked List Present in Array
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        elements = set(nums)
        ptr, prev = head, None
        while ptr:
            if ptr.val in elements:
                if ptr == head:
                    head = head.next
                    ptr = head
                else:
                    prev.next = ptr.next
                    ptr = ptr.next
            else:
                prev = ptr
                ptr = ptr.next
        return head


def test(nums: list[int], head: Optional[ListNode]):
    def print_all(ptr):
        while ptr:
            print(ptr.val, end=' ')
            ptr = ptr.next
        print()
    head = Solution().modifiedList(nums, head)
    print_all(head)


test(
    [1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
test(
    [1],
    ListNode(1,
             ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2)))))))
test([5], ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
