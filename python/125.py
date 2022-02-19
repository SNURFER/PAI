import collections


def isPalindrome(s: str) -> bool:
    modified_str: collections.deque = collections.deque()
    for ch in s:
        if ch.isalnum():
            modified_str.append(ch.lower())

    while len(modified_str) > 1:
        if modified_str.pop() != modified_str.popleft():
            return False
    return True


if __name__ == "__main__":
    s = "a man a plan a canal : panama!"
    print(isPalindrome(s))
