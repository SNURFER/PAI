# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list = []

        node = head
        while node:
            temp_list.append(node.val)
            node = node.next

        temp_list.sort()

        #don't need to assign new listnode...
        #just replace value of input node...
        sorted_node = None
        next_node = None
        while len(temp_list):
            val = temp_list.pop()
            sorted_node = ListNode(val)
            sorted_node.next, next_node = next_node, sorted_node

        return sorted_node


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(22)
    node4 = ListNode(17)
    node5 = ListNode(13)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    ret_node = solution.sortList(node1)

    while ret_node:
        print(ret_node.val)
        ret_node = ret_node.next