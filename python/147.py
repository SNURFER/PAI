# Definition for singly-linked list.
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(-sys.maxsize)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            head.next, cur.next, head = cur.next, head, head.next

            if head and head.val < cur.val:
                cur = parent

        return parent.next


if __name__ == "__main__":
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    ret_head = solution.insertionSortList(node1)

    while ret_head:
        print(ret_head.val)
        ret_head = ret_head.next
