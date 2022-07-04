def solution(begin, target, words):
    answer = 0
    visit = [False] * len(words)

    def dfs(depth: int, curent: str):
        nonlocal answer
        if depth == len(words) - 1:
            answer = 0
            return
        if curent == target:
            answer = depth
            return
        for i in range(len(words)):
            if can_convert(words[i], curent) and not visit[i]:
                visit[i] = True
                dfs(depth + 1, words[i])
                visit[i] = False

    def can_convert(str1: str, str2: str) -> bool:
        diff_cnter = 0
        for i in range(len(str1)):
            if str1[i] is not str2[i]:
                diff_cnter += 1
            if diff_cnter > 1:
                return False
        if diff_cnter == 0:
            return False
        return True

    dfs(0, begin)

    return answer


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin,target, words))
