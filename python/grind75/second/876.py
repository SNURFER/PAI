# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        slow_ptr: ListNode = head
        fast_ptr: ListNode = head

        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr




if __name__ == "__main__":
    node1: ListNode = ListNode(3)
    node2: ListNode = ListNode(2)
    node3: ListNode = ListNode(0)
    node4: ListNode = ListNode(4)
    node5: ListNode = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

