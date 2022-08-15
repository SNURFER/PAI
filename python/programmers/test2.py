import collections
import sys

def solution():
    N = int(sys.stdin.readline())

    edge_dict = collections.defaultdict(list)
    for _ in range(N):
        per1, per2 = map(int, sys.stdin.readline().split())
        edge_dict[per1].append(per2)
        edge_dict[per2].append(per1)

    visit = set()
    counter = 0

    def dfs(depart: int):
        if len(visit) == len(edge_dict):
            return

        visit.add(depart)
        for dest in edge_dict[depart]:
            if dest not in visit:
                dfs(dest)

    for key in edge_dict:
        if key not in visit and len(edge_dict[key]) > 0:
            counter += 1
            dfs(key)

    print(counter)


if __name__ == "__main__":

# 6
# 1 3
# 3 4
# 6 5
# 11 15
# 12 17
# 12 15
    solution()