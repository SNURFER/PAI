import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    s_card = list(map(int, input().split()))
    s_card_set = set()
    for num in s_card:
        s_card_set.add(num)

    m = int(input())
    inputs = list(map(int, input().split()))

    for num in inputs:
        if num not in s_card_set:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    solution()
