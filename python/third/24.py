# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head


if __name__ == "__main__":
    # head = [1, 2, 3, 4]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    ret_val = solution.swapPairs(node1)
    while ret_val:
        print(ret_val.val)
        ret_val = ret_val.next

