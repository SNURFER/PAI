# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pos: int = -1

        if not head:
            return False

        slow_ptr: ListNode = head

        if not head.next:
            return False

        fast_ptr: ListNode = head.next

        loop_ctr: int = -1
        while slow_ptr and fast_ptr and fast_ptr.next:
            loop_ctr += 1
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                pos = loop_ctr
                break

        return False if pos == -1 else True


if __name__ == "__main__":
    node1: ListNode = ListNode(3)
    node2: ListNode = ListNode(2)
    node3: ListNode = ListNode(0)
    node4: ListNode = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    solution = Solution()
    print(solution.hasCycle(node1))


