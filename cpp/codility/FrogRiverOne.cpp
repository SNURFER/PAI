#include <vector>
#include <iostream>
#include <set>

using namespace std;

int solution(int X, vector<int> &A) {
    set<int> leave;
    for (size_t i = 0; i < A.size(); i++) {
        leave.insert(A[i]);
        if (leave.size() == (unsigned)X) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> a = {1, 3, 1, 4, 2, 3, 5, 4};
    cout << solution(5, a) << endl;
    return 0;
}
