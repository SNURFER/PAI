# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode], lis2=None) -> Optional[ListNode]:
        head = ListNode()
        pre_node = head

        while list1 is not None and list2 is not None:
            head.next = ListNode()
            head = head.next
            if list1.val > list2.val:
                head.val = list2.val
                list2 = list2.next
            else:
                head.val = list1.val
                list1 = list1.next

        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return pre_node.next


if __name__ == "__main__":

    node1 = ListNode(5)
    node2 = ListNode(2, node1)
    node3 = ListNode(0, node2)

    node4 = ListNode(7)
    node5 = ListNode(3, node4)
    node6 = ListNode(0, node5)

    solution = Solution()
    merged_node = solution.mergeTwoLists(node3, node6)

    while merged_node:
        print(merged_node.val)
        merged_node = merged_node.next

