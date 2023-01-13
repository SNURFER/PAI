# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_walker = head
        fast_walker = head
        while slow_walker and fast_walker.next:
            slow_walker = slow_walker.next
            if not fast_walker.next.next:
                break
            fast_walker = fast_walker.next.next

        return slow_walker


if __name__ == "__main__":

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
    print(solution.middleNode(node1).val)

