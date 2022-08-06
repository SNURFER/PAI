import collections
import heapq
import sys

input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    K = int(input())
    INF = sys.maxsize

    edge_weight = collections.defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge_weight[u - 1].append((v - 1, w))

    depart = K - 1
    weight_from_k = [INF] * V
    weight_from_k[depart] = 0

    priority_idx = []
    heapq.heappush(priority_idx, (0, depart))
    while priority_idx:
        cur_weight, depart = heapq.heappop(priority_idx)

        for dest, weight in edge_weight[depart]:
            new_weight = cur_weight + weight
            if new_weight < weight_from_k[dest]:
                weight_from_k[dest] = new_weight
                heapq.heappush(priority_idx, (weight_from_k[dest], dest))

    for weight in weight_from_k:
        if weight != INF:
            print(weight)
        else:
            print("INF")


if __name__ == "__main__":
    solution()
