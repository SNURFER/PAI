#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int solution(vector<int> &D, vector<string> &T) {
    vector<map<char, int>> trash;

    int countP = 0;
    int countG = 0;
    int countM = 0;

    int longestP = 0;
    int longestG = 0;
    int longestM = 0;

    int idx = 0;
    for (auto t : T) {
        for (auto c : t) {
            if (c == 'P') {
                countP += 1;
                longestP = idx;
            }
            if (c == 'G') {
                countG += 1;
                longestG = idx;
            }
            if (c == 'M') {
                countM += 1;
                longestM = idx;
            }
        }
        idx += 1;
    }

    int sum = 0;
    for (size_t i = 0; i < D.size(); i++) {
        sum += D[i];
        D[i] = sum;
    }

    int pSum = 2 * D[longestP] + countP;
    int gSum = 2 * D[longestG] + countG;
    int mSum = 2 * D[longestM] + countM;

    return max(pSum, max(gSum, mSum));
}


int main() {
//    vector<int> d = {2, 5};
//    vector<string> t = {"PGP", "M"};
    vector<int> d = {2, 1, 1, 1, 2};
    vector<string> t = {"", "PP", "PP", "GM", ""};
    cout << solution(d, t) << endl;

}