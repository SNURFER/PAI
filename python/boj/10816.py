import collections
import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    s_card = list(map(int, input().split()))
    s_card_dict = collections.defaultdict(int)
    for num in s_card:
        s_card_dict[num] += 1

    m = int(input())
    inputs = list(map(int, input().split()))

    for num in inputs:
        print(s_card_dict[num])


if __name__ == "__main__":
    solution()
