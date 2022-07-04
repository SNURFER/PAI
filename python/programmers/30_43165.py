def solution(numbers, target):
    answer = 0

    def dfs(depth: int, accum: int):
        if depth == len(numbers) - 1:
            if accum == target:
                nonlocal answer
                answer += 1

            return

        dfs(depth + 1, accum + numbers[depth])
        dfs(depth + 1, accum - numbers[depth])

    dfs(-1, 0)

    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
