import collections
import heapq
import sys

input = sys.stdin.readline

def solution():
    edge_info = collections.defaultdict(list)
    v = int(input())
    data = [list(map(int, input().split())) for _ in range(v)]

    for row in data:
        for i in range(0, len(row) // 2 - 1):
            edge_info[row[0]].append(tuple((row[2 * i + 1], row[2 * i + 2])))

    max_distance = 0

    def dfs(node: int, parent: int) -> int:
        # only from parent
        if len(edge_info[node]) == 1 and parent != -1:
            return 0

        max_depth = []
        for dest in edge_info[node]:
            if dest[0] != parent:
                heapq.heappush(max_depth, -dfs(dest[0], node) - dest[1])

        max1, max2 = 0, 0
        if len(max_depth):
            max1 = -heapq.heappop(max_depth)
        if len(max_depth):
            max2 = -heapq.heappop(max_depth)

        nonlocal max_distance
        max_distance = max(max_distance, max1 + max2)
        return max1

    dfs(list(edge_info.keys())[0], -1)
    print(max_distance)


if __name__ == "__main__":
    solution()
