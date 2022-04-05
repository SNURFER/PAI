# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_deque = collections.deque([])

        while head:
            val_deque.append(head.val)
            head = head.next

        while val_deque:
            left = val_deque.popleft()

            if not val_deque:
                return True

            right = val_deque.pop()

            if left != right:
                return False

        return True


if __name__ == "__main__":
    node1: ListNode = ListNode(1)
    node2: ListNode = ListNode(2)
    node3: ListNode = ListNode(2)
    node4: ListNode = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    print(solution.isPalindrome(node1))
