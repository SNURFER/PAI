# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next

        if vals == vals[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    node4 = ListNode(1, None)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()
    print(solution.isPalindrome(node1))
