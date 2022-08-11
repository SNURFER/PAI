#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> &A) {
    int n = A.size();
    int missingVal = n + 1;

    for (size_t i = 0; i < n; i++) {
        missingVal = missingVal + (i + 1) - A[i];
    }
    return missingVal;
}
int main() {
    vector<int> a = {2, 3, 1, 6, 4};
    cout << solution(a) << endl;
    return 0;
}
