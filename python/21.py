
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#TODO assign object by = operator is hard...
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

        # sorted_node = None
        # node1, node2 = l1, l2
        # while node1 is not None and node2 is not None:
        #     if node1.val > node2.val:
        #         sorted_node = ListNode(node2.val, sorted_node)
        #         node2 = node2.next
        #     else:
        #         sorted_node = ListNode(node1.val, sorted_node)
        #         node1 = node1.next
        # while node1 is not None:
        #     sorted_node = ListNode(node1.val, sorted_node)
        #     node1 = node1.next
        # while node2 is not None:
        #     sorted_node = ListNode(node2.val, sorted_node)
        #     node2 = node2.next
        #
        # return sorted_node


if __name__ == "__main__":
    solution = Solution();

    node6 = ListNode(4, None)
    node5 = ListNode(3, node6)
    node4 = ListNode(1, node5)

    node3 = ListNode(4, None)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    print(solution.mergeTwoLists(node1, node4))
