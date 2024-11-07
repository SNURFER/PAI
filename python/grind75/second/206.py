# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


        # tail = None
        # while head:
        #     node = ListNode(head.val)
        #     node.next = tail
        #     node.next, tail = tail, node
        #     head = head.next
        #
        # return tail


if __name__ == "__main__":
    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    ret_val = solution.reverseList(node1)

    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next