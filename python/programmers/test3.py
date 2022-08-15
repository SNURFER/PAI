def solution(s):
    def dfs(s: str, depth: int, path: [], address):
        if depth == 4:
            if not s:
                address.append(path[:])
            return

        # if not depth 0, add delimiter to address
        if not depth == 0:
            path += "."

        for i in range(len(s)):
            # if 0, get next step
            if s[:i + 1] == '0' or (s[0] != '0' and 0 < int(s[:i + 1]) < 256):
                dfs(s[i + 1:], depth + 1, path + s[:i + 1], address)

    # under 4 or over 12 can't be IPv4 0.0.0.0 ~ 255.255.255.255
    if not 4 <= len(s) <= 12:
        return []

    addresses = []
    dfs(s, 0, "", addresses)
    print(len(addresses))
    for address in addresses:
        print(address)


if __name__ == "__main__":
    s = input()
    solution(s)