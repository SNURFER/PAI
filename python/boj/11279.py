import heapq
import sys

input = sys.stdin.readline

def solution():
    heap = []

    n = int(input())
    for _ in range(n):
        input_num = int(input())
        if input_num == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(-heap[0])
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, -input_num)


if __name__ == "__main__":
    solution()
