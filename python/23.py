# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = node_ptr = ListNode()

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            # node_ptr.val = node[0]
            node_ptr.next = node[2]
            node_ptr = node_ptr.next

            if node_ptr.next:
                heapq.heappush(heap, (node_ptr.next.val, idx, node_ptr.next))

        return head.next


if __name__ == "__main__":
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(2)
    node8 = ListNode(6)
    node7.next = node8

    input = [node1, node4, node7]
    output = solution.mergeKLists(input)

    while output:
        print(output.val)
        output = output.next
