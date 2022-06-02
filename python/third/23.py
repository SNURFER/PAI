# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p_queue = []
        head = node = ListNode();

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(p_queue, (lists[i].val, i, lists[i]))

        while p_queue:
            least_item = heapq.heappop(p_queue)
            idx = least_item[1]
            node.next = least_item[2]
            node = node.next

            if node.next:
                heapq.heappush(p_queue, (node.next.val, idx, node.next))

        return head.next


if __name__ == "__main__":
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
    input2 = [[]]

    solution = Solution()
    ret_val = solution.mergeKLists(input2)

    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next
