from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head


if __name__ == "__main__":
    solution = Solution()

    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    output_head = solution.swapPairs(node1)

    while output_head is not None:
        print(output_head.val)
        output_head = output_head.next

