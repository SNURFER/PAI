class MyQueue:

    def __init__(self):
        self.stack_l = []
        self.stack_r = []

    def push(self, x: int) -> None:
        while self.stack_l:
            item = self.stack_l.pop()
            self.stack_r.append(item)

        self.stack_l.append(x)

        while self.stack_r:
            item = self.stack_r.pop()
            self.stack_l.append(item)

    def pop(self) -> int:
        return self.stack_l.pop()

    def peek(self) -> int:
        return self.stack_l[-1]

    def empty(self) -> bool:
        return len(self.stack_l) == 0


if __name__ == "__main__":

    # Your MyQueue object will be instantiated and called as such:
    x_1 = 10
    x_2 = 20

    obj = MyQueue()
    obj.push(x_1)
    obj.push(x_2)

    print(obj.pop())
    print(obj.peek())
    print(obj.empty())

