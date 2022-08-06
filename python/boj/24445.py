import collections
import sys

input = sys.stdin.readline

def solution():
    n, m, r = map(int, input().split())
    adjacency_list = collections.defaultdict(list)
    queue = collections.deque([])

    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    start = r
    queue.append(start)
    visit = set()
    visit.add(start)

    visit_order = 1
    ret_val = [0] * (n + 1)
    while queue:
        item = queue.popleft()
        ret_val[item] = visit_order
        visit_order += 1
        for dest in sorted(adjacency_list[item], key=lambda x: -x):
            if dest not in visit:
                visit.add(dest)
                queue.append(dest)

    for val in ret_val[1:]:
        print(val)


if __name__ == "__main__":
    solution()
