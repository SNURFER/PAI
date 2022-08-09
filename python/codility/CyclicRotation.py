# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    ans = [0] * len(A)
    for i in range(len(A)):
        ans[(i + K) % len(A)] = A[i]

    return ans


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print(solution(A, 3))
