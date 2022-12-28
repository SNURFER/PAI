from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        reverse_node = None
        while head:
            tmp_node = reverse_node
            while reverse_node:
                if head is reverse_node:
                    return True
                reverse_node = reverse_node.next
            reverse_node = tmp_node

            head, unlink_node = head.next, head
            unlink_node.next, reverse_node = reverse_node, unlink_node

        return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = node2

    solution = Solution()
    print(solution.hasCycle(node1))
