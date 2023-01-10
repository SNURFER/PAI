

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_node = None

        while head:
            head.next, reverse_node, temp = reverse_node, head, head.next
            head = temp

        return reverse_node


if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    ret_node = solution.reverseList(node1)

    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next
