import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    n_n = [[0] * (n + 1) for _ in range(n + 1)]
    data = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 그냥 sum을 해버리면 range 밖으로 넘어가는 sum을 처리 못하니까 dp로 해야함
            n_n[i][j] = n_n[i][j - 1] + n_n[i - 1][j] - n_n[i - 1][j - 1] + data[i - 1][j - 1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        ans = n_n[x2][y2] - n_n[x1 - 1][y2] - n_n[x2][y1 - 1] + n_n[x1 - 1][y1 - 1]
        print(ans)


if __name__ == "__main__":
    solution()
