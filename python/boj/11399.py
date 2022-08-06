import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    person_sorted = list(map(int, input().split()))
    person_sorted.sort()

    accum_time = 0
    total_sum = 0
    for person in person_sorted:
        accum_time += person
        total_sum += accum_time

    return total_sum


if __name__ == "__main__":
    print(solution())
