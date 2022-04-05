# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None

        while head:
            parent_node = ListNode(head.val)
            parent_node.next = prev_node
            prev_node = parent_node
            head = head.next

        return prev_node


if __name__ == "__main__":

    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()
    ret_node = solution.reverseList(node1)

    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next

