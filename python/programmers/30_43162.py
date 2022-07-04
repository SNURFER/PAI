def solution(n, computers):
    visit = [False] * n

    def dfs(target: int):
        for i in range(n):
            if visit[i] == False and computers[target][i] == 1:
                visit[i] = True
                dfs(i)

    answer = 0
    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            answer += 1
            dfs(i)

    return answer


if __name__ == "__main__":
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    n = 3
    print(solution(n, computers))
