# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort_list = []
        node = head
        while node:
            heapq.heappush(sort_list, node.val)
            node = node.next

        node = head
        while node:
            node.val = heapq.heappop(sort_list)
            node = node.next

        return head


if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(4)
    node4 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    ret_node = solution.sortList(node1)
    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next

