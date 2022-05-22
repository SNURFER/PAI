# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = merged_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                merged_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged_node.next = ListNode(list2.val)
                list2 = list2.next

            merged_node = merged_node.next

        while list1:
            merged_node.next = ListNode(list1.val)
            list1 = list1.next
            merged_node = merged_node.next

        while list2:
            merged_node.next = ListNode(list2.val)
            list2 = list2.next
            merged_node = merged_node.next

        return head.next


if __name__ == "__main__":
    # list1 = [1, 2, 4], list2 = [1, 3, 4]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    solution = Solution()
    ret_val = solution.mergeTwoLists(node1, node4)

    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next
