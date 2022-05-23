# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev_node = None
        while head:
            node = ListNode(head.val)
            node.next = prev_node
            prev_node = node
            head = head.next

        return node


if __name__ == "__main__":
    # head = [1, 2, 3, 4, 5]
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
    ret_val = solution.reverseList([])
    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next
