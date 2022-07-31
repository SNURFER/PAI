import sys


class Heap:
    heap_items = []

    def insert(self, input: int):
        self.heap_items.append(input)
        child_idx = self.length() - 1
        parent_idx = (child_idx - 1) // 2

        while child_idx > 0:
            if self.heap_items[child_idx] < self.heap_items[parent_idx]:
                self.heap_items[child_idx], self.heap_items[parent_idx] = \
                    self.heap_items[parent_idx], self.heap_items[child_idx],

                child_idx = parent_idx
                parent_idx = (child_idx - 1) // 2
            else:
                break

    def pop(self) -> int:
        ret_val = self.heap_items[0]
        self.heap_items[0], self.heap_items[-1] = self.heap_items[-1], self.heap_items[0]
        self.heap_items.pop()
        self.heapify(0)

        return ret_val

    def heapify(self, root_idx: int):
        left_idx = 2 * root_idx + 1
        right_idx = left_idx + 1

        high_priority_idx = root_idx
        if left_idx < self.length():
            if self.heap_items[root_idx] > self.heap_items[left_idx]:
                high_priority_idx = left_idx

        if right_idx < self.length():
            if self.heap_items[high_priority_idx] > self.heap_items[right_idx]:
                high_priority_idx = right_idx

        if high_priority_idx is not root_idx:
            self.heap_items[high_priority_idx], self.heap_items[root_idx] = \
                self.heap_items[root_idx], self.heap_items[high_priority_idx]
            self.heapify(high_priority_idx)

    def length(self) -> int:
        return len(self.heap_items)


def solution():
    heap = Heap()

    N = int(sys.stdin.readline())

    for i in range(N):
        num = int(sys.stdin.readline())
        if num > 0:
            heap.insert(num)
        if num == 0:
            if heap.length() == 0:
                print(0)
            else:
                print(heap.pop())


if __name__ == "__main__":
    solution()
