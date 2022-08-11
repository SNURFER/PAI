#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> &A) {
    if (A.size() < 3) return 0;
    // write your code in C++14 (g++ 6.2.0)
    sort(A.begin(), A.end());

    bool hasTriangular = false;

    for (size_t i = 0; i < A.size() - 2; i++) {
        if (A[i] > A[i + 2] - A[i + 1]) {
            hasTriangular = true;
            break;
        }
    }
    if (hasTriangular) return 1;
    return 0;
}

int main() {
    vector<int> a = {10, 2, 5, 1, 8, 20};
    cout << solution(a) << endl;
}