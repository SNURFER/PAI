# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mirror_node: ListNode = head

        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head.next = head.next.next

            head = head.next

        return mirror_node


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(5)
    node5 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    ret_node: ListNode = solution.deleteDuplicates(node1)

    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next


