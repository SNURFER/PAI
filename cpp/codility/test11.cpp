#include <vector>
#include <iostream>
#include <map>
#define MAX_RESULT 1000000000
using namespace std;

int solution(vector<int> &A, int S) {
    int countAnswer = 0;
    int curSum = 0;
    map<int, int> avgFreq;

    for (size_t i = 0; i < A.size(); i++) {
        curSum += (A[i] - S);
        if (curSum == 0)
            countAnswer += 1;
        if (avgFreq.find(curSum) != avgFreq.end())
            countAnswer += avgFreq[curSum];
        if (countAnswer > MAX_RESULT)
            return MAX_RESULT;

        avgFreq[curSum] += 1;
    }

    return countAnswer;
}

int main() {
    vector<int> a = {0, 4, 3, -1};
    int s = 2;
    cout << solution(a, s) << endl;


}