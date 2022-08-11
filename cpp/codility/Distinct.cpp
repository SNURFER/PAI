#include <vector>
#include <iostream>
#include <set>

using namespace std;


int solution(vector<int> &A) {
    set<int> distinctVal;

    for (auto a : A) {
        distinctVal.insert(a);
    }
    return (unsigned)distinctVal.size();
}

int main() {
    vector<int> a = {2, 1, 1, 2, 3, 1};
    cout << solution(a) << endl;
    return 0;
}
