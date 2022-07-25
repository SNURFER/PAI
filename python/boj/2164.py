import collections


def solution(n: int) -> int:
    queue = collections.deque([])
    for i in range(1, n + 1):
        queue.append(i)

    while len(queue) > 1:
        queue.popleft()
        item = queue.popleft()
        queue.append(item)

    return queue.popleft()


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
