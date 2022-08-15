#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int solution(vector<int> &D, vector<string> &T) {
    vector<map<char, int>> trash;

    int maxPIdx = -1;
    int maxGIdx = -1;
    int maxMIdx = -1;

    // organize trash by map
    for (auto t : T) {
        map<char, int> houseTrash;
        for (auto c : t) {
            // if exist
            if (houseTrash.find(c) != houseTrash.end()) {
                houseTrash[c] += 1;
            } else {
                houseTrash.insert({c, 1});
            }
        }
        trash.push_back(houseTrash);
    }

    // accumulate sum of distance
    int sum = 0;
    for (size_t i = 0; i < D.size(); i++) {
        sum += D[i];
        D[i] = sum;
    }

    int pSum = 0;
    int gSum = 0;
    int mSum = 0;

    for (size_t i = 0; i < D.size(); i++) {
        int roundTrip = 2 * D[i];

        // has P
        if (trash[i].find('P') != trash[i].end()) {
            pSum += trash[i]['P'] + roundTrip;
        }

        // has G
        if (trash[i].find('G') != trash[i].end()) {
            gSum += trash[i]['G'] + roundTrip;
        }

        // has M
        if (trash[i].find('M') != trash[i].end()) {
            mSum += trash[i]['M'] + roundTrip;
        }
    }

    return max(pSum, max(gSum, mSum));

}


int main() {
//    vector<int> d = {2, 5};
//    vector<string> t = {"PGP", "M"};
    vector<int> d = {2, 1, 1, 1, 2};
    vector<string> t = {"", "PP", "PP", "GM", ""};
    cout << solution(d, t) << endl;

}