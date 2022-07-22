# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node_queue = collections.deque([cloned])

        while node_queue:
            item = node_queue.popleft()
            if item.val == target.val:
                return item

            if item.left:
                node_queue.append(item.left)
            if item.right:
                node_queue.append(item.right)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    node1c = TreeNode(1)
    node2c = TreeNode(2)
    node3c = TreeNode(3)
    node4c = TreeNode(4)
    node5c = TreeNode(5)

    node1c.left = node2c
    node1c.right = node3c
    node3c.left = node4c
    node3c.right = node5c

    solution = Solution()
    ret_node = solution.getTargetCopy(node1, node1c, node3)

    print(ret_node.val)

