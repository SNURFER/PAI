# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        sorted = []
        while node:
            heapq.heappush(sorted, node.val)
            node = node.next

        node = head

        while node:
            node.val = heapq.heappop(sorted)
            node = node.next
        return head


if __name__ == "__main__":
    # head = [4, 2, 1, 3]
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    ret_val = solution.sortList(node1)
    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next
