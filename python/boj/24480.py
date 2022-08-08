import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    n, m, r = map(int, input().split())
    adjacency_list = collections.defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visit = set()

    visit_order = 1
    ret_val = [0] * (n + 1)

    def dfs(depart: int):
        nonlocal visit_order
        visit.add(depart)
        ret_val[depart] = visit_order
        visit_order += 1

        for dest in sorted(adjacency_list[depart], key=lambda x: -x):
            if dest not in visit:
                dfs(dest)

    dfs(r)
    for val in ret_val[1:]:
        print(val)


if __name__ == "__main__":
    solution()
