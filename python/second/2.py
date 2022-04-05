# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_left = []
        num_right = []

        while l1:
            num_left.append(str(l1.val))
            l1 = l1.next

        while l2:
            num_right.append(str(l2.val))
            l2 = l2.next

        plus_val = int(''.join(num_left[::-1])) + int(''.join(num_right[::-1]))

        if plus_val == 0:
            return ListNode(0)

        head = node = ListNode()
        while plus_val > 0:
            node.next = ListNode(plus_val % 10)
            node = node.next
            plus_val = plus_val // 10

        return head.next


if __name__ == '__main__':

    node6 = ListNode(4, None)
    node5 = ListNode(6, node6)
    node4 = ListNode(5, node5)

    node3 = ListNode(3, None)
    node2 = ListNode(4, node3)
    node1 = ListNode(2, node2)

    # node4 = ListNode(0, None)
    # node1 = ListNode(0, None)
    solution = Solution()
    ret_node = solution.addTwoNumbers(node1, node4)
    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next
