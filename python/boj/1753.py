import heapq
import sys


def solution():
    V, E = map(int, input().split())
    K = int(input())

    edge_weight = [[sys.maxsize] * V for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        # if more than two edges with same direction between 2 vertex,
        # only smaller weight is saved in edge_weight
        edge_weight[u - 1][v - 1] = min(edge_weight[u - 1][v - 1], w)

    depart = K - 1
    weight_from_k = [sys.maxsize] * V
    weight_from_k[depart] = 0

    visit = set()
    visit.add(depart)
    priority_idx = []
    while len(visit) < V:
        for dest in range(len(edge_weight[depart])):
            # check edge between depart -> dest
            if edge_weight[depart][dest] != sys.maxsize:
                weight_from_k[dest] = min(weight_from_k[dest], weight_from_k[depart] + edge_weight[depart][dest])
                heapq.heappush(priority_idx, (weight_from_k[dest], dest))

        if len(priority_idx) == 0:
            break

        _, dest = heapq.heappop(priority_idx)
        depart = dest
        visit.add(dest)
        priority_idx.clear()

    for weight in weight_from_k:
        if weight != sys.maxsize:
            print(weight)
        else:
            print("INF")


if __name__ == "__main__":
    solution()
