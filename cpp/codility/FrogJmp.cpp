#include <vector>
#include <iostream>

using namespace std;

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int X, int Y, int D) {
    return (Y - X + (D - 1)) / D;
    // write your code in C++14 (g++ 6.2.0)
}


int main() {
    int x = 10;
    int y = 85;
    int z = 30;

    cout << solution(x, y, z) << endl;

    return 0;
}
