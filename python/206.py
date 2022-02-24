from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#TODO assign object by = operator is hard...
class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            # prev, prev.next = node, prev
            # node = node.next
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


if __name__ == '__main__':

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution();
    output_head = solution.reverseList(node1)

    while output_head is not None:
        print(output_head.val)
        output_head = output_head.next

