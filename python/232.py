class MyQueue:

    def __init__(self):
        self.stack = []
        self.rebaser = []

    def push(self, x: int) -> None:
        while self.stack:
            self.rebaser.append(self.stack.pop())
        self.stack.append(x)
        while self.rebaser:
            self.stack.append(self.rebaser.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.peek() # 1 return
    param_3 = obj.pop() # 1 return
    param_4 = obj.empty() # False

    print (param_2, ' ', param_3, ' ', param_4)