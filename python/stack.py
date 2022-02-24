class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.last_node: ListNode = None

    def push(self, val):
        self.last_node = ListNode(val, self.last_node)
        print(val, ': has pushed')

    def pop(self) -> int:
        val = self.last_node.val
        self.last_node = self.last_node.next
        print(val, ': has popped')
        return val


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.push(3)
    stack.pop()
    stack.push(4)
    stack.push(5)
    stack.pop()
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
