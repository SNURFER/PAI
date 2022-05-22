# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums == nums[::-1]


if __name__ == "__main__":
    # head = [1, 2, 2, 1]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    print(solution.isPalindrome(node1))

