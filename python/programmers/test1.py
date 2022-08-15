def solution():
    a, b = map(str, input().strip().split(' '))

    # number of delimeters
    D = len(a)
    # number of elements
    L = len(b)

    # print number of joined lists
    print(D ** (L - 1))

    def dfs(depth: int, path: []):
        if depth == L - 1:
            path.append(b[L - 1])
            print(''.join(path))
            return

        for delim in a:
            dfs(depth + 1, path + [str(b[depth]), delim])

    dfs(0, [])


if __name__ == "__main__":
    solution()