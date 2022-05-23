# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left_num = collections.deque([])
        right_num = collections.deque([])

        while l1:
            left_num.appendleft(str(l1.val))
            l1 = l1.next

        while l2:
            right_num.appendleft(str(l2.val))
            l2 = l2.next

        num_l = 0 if len(left_num) == 0 else int(''.join(left_num))
        num_r = 0 if len(left_num) == 0 else int(''.join(right_num))

        sum_num = num_l + num_r

        prev_node = None
        for num in list(str(sum_num)):
            node = ListNode(num)
            node.next = prev_node
            prev_node = node

        return node


if __name__ == "__main__":
    # l1 = [2, 4, 3], l2 = [5, 6, 4]
    node_l = ListNode(2)
    node_l_2 = ListNode(4)
    node_l_3 = ListNode(3)
    node_l.next = node_l_2
    node_l_2.next = node_l_3

    node_r = ListNode(5)
    node_r_2 = ListNode(6)
    node_r_3 = ListNode(4)
    node_r.next = node_r_2
    node_r_2.next = node_r_3

    solution = Solution()
    # ret_val = solution.addTwoNumbers(node_l, node_r)
    ret_val = solution.addTwoNumbers(None, None)
    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next

