class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        while self.pop_stack:
            item = self.pop_stack.pop()
            self.push_stack.append(item)

        self.push_stack.append(x)

    def pop(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        elif self.push_stack:
            while self.push_stack:
                item = self.push_stack.pop()
                self.pop_stack.append(item)
            return self.pop_stack.pop()

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        elif self.push_stack:
            while self.push_stack:
                item = self.push_stack.pop()
                self.pop_stack.append(item)
            return self.pop_stack[-1]

    def empty(self) -> bool:
        if not self.pop_stack and not self.push_stack:
            return True
        return False


if __name__ == "__main__":

    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(3)
    obj.push(4)
    obj.push(5)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    obj.push(6)
    obj.push(7)
    param_5 = obj.peek()
    param_6 = obj.pop()


    print(param_2, param_3, param_4, param_5, param_6)
