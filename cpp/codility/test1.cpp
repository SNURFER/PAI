#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> &A, int S) {
    int countAnswer = 0;
    int curLength;

    // two pointer solution
    // locate left and calculate all average with position right
    // if average == S count up
    // l means left
    for (size_t l = 0; l < A.size(); l++) {
        int curSum = 0;
        // r means right
        for (size_t r = l; r < A.size(); r++) {
            curSum += A[r];
            curLength = r - l + 1;

            if (curSum % curLength == 0 && curSum / curLength == S) countAnswer += 1;
        }
        if (countAnswer == 1000000000) {
            return countAnswer;
        }
    }

    return countAnswer;
}

int main() {
    vector<int> a = {2, 1, 3};
    int s = 2;
    cout << solution(a, s) << endl;


}