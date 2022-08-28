import sys
from typing import List

input = sys.stdin.readline


def solution():
    n: int = int(input());
    nums: List[int] = [0]
    dp: List[int] = [0] * (n + 1)

    for _ in range(n):
        nums.append(int(input()))

    lis = 0
    for i in range(1, n + 1):
        dp[i] = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])

        lis = max(lis, dp[i])

    return n - lis


if __name__ == "__main__":
    print(solution())
