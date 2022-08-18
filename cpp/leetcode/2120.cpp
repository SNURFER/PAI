#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    pair<int, int> getDirection(char ch) {
        if (ch == 'R')
            return make_pair(0, 1);
        if (ch == 'L')
            return make_pair(0, -1);
        if (ch == 'D')
            return make_pair(1, 0);
        if (ch == 'U')
            return make_pair(-1, 0);

        else
            return make_pair(0, 0);
    }

    bool isInRange(int x, int y, int n) {
        if (x < 0) return false;
        if (y < 0) return false;
        if (x > n - 1) return false;
        if (y > n - 1) return false;

        return true;
    }

    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        vector<int> retVec(s.size(), 0);

        for (size_t i = 0; i < s.size(); i++) {
            vector<int> inputPos = startPos;
            int countExecute = 0;
            int j = i;
            char ins = s[j];
            while (j < s.size() && isInRange(inputPos[0] + getDirection(ins).first, inputPos[1] + getDirection(ins).second, n)) {
                inputPos[0] = inputPos[0] + getDirection(ins).first;
                inputPos[1] = inputPos[1] + getDirection(ins).second;
                countExecute += 1;
                j += 1;
                ins = s[j];
            }
            retVec[i] = countExecute;
        }
        return retVec;
    }
};

int main() {
    int n = 3;
    vector<int> startPos = {0,1};
    string s = "RRDDLU";
    Solution solution;
    auto ret = solution.executeInstructions(n, startPos, s);
    for (auto item : ret) {
        cout << item << endl;
    }

    return 0;
}
