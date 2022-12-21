from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root_left = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                head.next, list1 = list1, list1.next
            else:
                head.next, list2 = list2, list2.next

            head = head.next

        if list2:
            head.next = list2
        if list1:
            head.next = list1

        return root_left.next


if __name__ == "__main__":
    # node1_1 = ListNode(1)
    # node1_2 = ListNode(2)
    # node1_3 = ListNode(4)
    #
    # node1_1.next = node1_2
    # node1_2.next = node1_3
    #
    # node2_1 = ListNode(1)
    # node2_2 = ListNode(3)
    # node2_3 = ListNode(4)
    #
    # node2_1.next = node2_2
    # node2_2.next = node2_3
    node1_1 = None
    node2_1 = None

    solution = Solution()
    ans = solution.mergeTwoLists(node1_1, node2_1)

    while ans:
        print(ans.val)
        ans = ans.next
