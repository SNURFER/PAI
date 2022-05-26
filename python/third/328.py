# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        odd = odd_head = head
        even = even_head = head.next

        head = head.next.next

        while head and head.next:
            odd.next = head
            even.next = head.next
            head, odd, even = head.next.next, odd.next, even.next

        if head:
            odd.next = head
            odd = odd.next
            even.next = None

        odd.next = even_head
        return odd_head


if __name__ == '__main__':
    # head = [1, 2, 3, 4, 5]

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    # node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6

    solution = Solution()
    ret_node = solution.oddEvenList(node1)
    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next
