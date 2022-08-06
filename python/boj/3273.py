import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    target = int(input())

    left, right = 0, len(numbers) - 1

    counter = 0
    while left < right:
        if numbers[left] + numbers[right] == target:
            counter += 1
            left += 1
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

    return counter


if __name__ == "__main__":
    print(solution())

