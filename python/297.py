# Definition for a binary tree node.
import collections
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root) -> str:
        pickles = ['#']
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)
                pickles.append(str(node.val))
            else:
                pickles.append('#')

        return ' '.join(pickles)

    def deserialize(self, data: str) -> TreeNode:
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(nodes[1])
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if index < len(nodes) and nodes[index] != '#':
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1

            if index < len(nodes) and nodes[index] != '#':
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1

        return root


if __name__ == "__main__":
    node4 = TreeNode(5)
    node2 = TreeNode(-3)
    node2.left = node4
    node3 = TreeNode(2)
    node1 = TreeNode(1)
    node1.left = node2
    node1.right = node3

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(node1))
    print(ser.serialize(node1))
    print(ser.serialize((ans)))
    # print(ser.serialize([]))
    # print(deser.deserialize(ser.serialize(([]))))
