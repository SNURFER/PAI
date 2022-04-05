# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        while list1:
            node.next = ListNode(list1.val)
            list1 = list1.next
            node = node.next

        while list2:
            node.next = ListNode(list2.val)
            list2 = list2.next
            node = node.next

        return head.next


if __name__ == "__main__":
    node3 = ListNode(4, None)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    node6 = ListNode(4, None)
    node5 = ListNode(3, node6)
    node4 = ListNode(1, node5)

    solution = Solution()
    ret_head = solution.mergeTwoLists(node1, node4)

    while ret_head:
        print(ret_head.val)
        ret_head = ret_head.next

