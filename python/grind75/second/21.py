# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head: ListNode = ListNode()
        node_ptr = head

        while list1 and list2:
            if list1.val < list2.val:
                cur_node = list1
                list1 = list1.next
            else:
                cur_node = list2
                list2 = list2.next

            node_ptr.next = cur_node
            node_ptr = node_ptr.next

        if list1 is not None:
            node_ptr.next = list1
        if list2 is not None:
            node_ptr.next = list2

        return head.next


if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2

    node3 = ListNode(3)
    node4 = ListNode(4)

    node3.next = node4

    solution = Solution()
    ret_val = solution.mergeTwoLists(node1, node3)

    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next