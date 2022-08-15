from bisect import bisect, bisect_left
import sys


def solution():
    N = int(sys.stdin.readline())
    dp = [[0, 0, []]]  # endTime, profit, path

    def binarySearch(time):
        low, high = 0, len(dp)
        while low < high:
            mid = (low + high) // 2
            if time < dp[mid][0]:
                high = mid
            else:
                low = mid + 1
        return low - 1

    # task item is [end, start, reward]
    tasks = []
    for _ in range(N):
        start, duration, reward = map(int, sys.stdin.readline().split())
        tasks.append([start + duration, start, reward])

    for end, start, reward in tasks:
        latest = binarySearch(start)
        if dp[latest][1] + reward > dp[-1][1]:
            dp.append([end, dp[latest][1] + reward, dp[latest][2] + [[start, end]]])

    print(dp[-1][-2])
    for task in dp[-1][-1]:
        print(task[0], task[1] - task[0])


if __name__ == "__main__":
    # 5
    # 0 4 5
    # 3 4 20
    # 6 6 3
    # 8 5 35
    # 10 4 12
    solution()