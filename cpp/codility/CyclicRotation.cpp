#include <iostream>
#include <vector>

using namespace std;
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// std::cout << "this is a debug message" << std::endl;

vector<int> solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    vector<int> rotatedVec(A.size(), 0);
    int n = A.size();
    for (int i = 0; i < n; i++) {
        rotatedVec[(i + K) % n] = A[i];
    }
    return rotatedVec;
}


int main() {
    cout << "Hello, World!" << endl;
    vector<int> a = {3, 4, 5, 6, 7};
    int k = 3;
    solution(a, k);

    return 0;
}
