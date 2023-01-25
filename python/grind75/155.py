import heapq
from collections import deque


class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.mins) or (self.mins[-1] >= val):
            self.mins.append(val)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if self.mins[-1] is pop_val:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minimums = deque()
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#
#         if self.minimums and val <= self.minimums[0]:
#             self.minimums.appendleft(val)
#             return
#         self.minimums.append(val)
#
#     def pop(self) -> None:
#         val = self.stack.pop()
#         if self.minimums[0] == val:
#             self.minimums.popleft()
#             return
#         self.minimums.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return min(self.minimums[0], self.minimums[-1])


if __name__ == "__main__":

    val1 = 512
    val2 = -1024
    val3 = -1024
    val4 = 512
    obj = MinStack()
    obj.push(val1)
    obj.push(val2)
    obj.push(val3)
    obj.push(val4)
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
