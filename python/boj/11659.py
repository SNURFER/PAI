import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    accum_num = [0]
    cur_sum = 0
    for num in numbers:
        cur_sum += num
        accum_num.append(cur_sum)

    for _ in range(m):
        s_idx, e_idx = map(int, input().split())
        print(accum_num[e_idx] - accum_num[s_idx - 1])


if __name__ == "__main__":
    solution()
