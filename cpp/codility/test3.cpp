#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int solution(vector<int> &A) {
    int left = 0;
    int n = A.size();

    int preVal;
    int firstIdx;
    int secondIdx;
    int maxLength = 0;

    if (n == 1) return 1;

    while (left < n) {
        set<int> biStorage;
        biStorage.insert(A[left]);
        firstIdx = left;
        secondIdx = left;
        preVal = A[left];
        for (int right = left + 1; right < n; right++) {
            biStorage.insert(A[right]);

            if (biStorage.size() <= 2) {
                if (preVal != A[right]) {
                    firstIdx = right - 1;
                    secondIdx = right;
                }
            } else {
                maxLength = max(maxLength, right - left);
                left = max(firstIdx, secondIdx);
                break;
            }

            preVal = A[right];
            if (right == n - 1) {
                maxLength = max(maxLength, right - left + 1);
                left = n;
                break;
            }
        }
    }
    return maxLength;
}

int main() {

//    vector<int> a = {0, 5, 4, 4, 5, 12};
    vector<int> a = {1, 1, 1, 1};

    cout << solution(a) << endl;



}