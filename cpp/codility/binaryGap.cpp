#include <iostream>

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// std::cout << "this is a debug message" << std::endl;

int solution(int N) {
    bool isGapMode = false;
    int zeroCount = 0;
    int maxZeroCount = 0;
    while (N > 0) {
        int mod = N % 2;
        if (mod == 1) {
            if (isGapMode) {
                maxZeroCount = std::max(maxZeroCount, zeroCount);
            } else{
                isGapMode = true;
            }
            zeroCount = 0;
        } else {
            zeroCount += 1;
        }
        N /= 2;
    }
    std::cout << maxZeroCount << std::endl;

    return maxZeroCount;

}

int main() {
    std::cout << "Hello, World!" << std::endl;
    int n = 529;
    solution(n);
    return 0;
}
