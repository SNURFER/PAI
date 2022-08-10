# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    return (Y - X + D - 1) // D


if __name__ == "__main__":
    print(solution(10, 85, 30))