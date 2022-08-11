
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> dp(100001, -1);

int recurCalBits(int n) {
    if (dp[n] != -1) return dp[n];
    int numOnes = recurCalBits(n / 2) + n % 2;

    return dp[n] = numOnes;
}

vector<int> countBits(int n) {
    vector<int> output;
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 0; i <= n; i++) {
        output.push_back(recurCalBits(i));
    }

    return output;
}

int main() {

    int input = 11;

    vector<int> output = countBits(input);

    for (int i = 0; i <= input; i++) {
        cout << output[i] << endl;;
    }

    for (auto bit : output) {
        cout << bit << endl;
    }

    return 0;
}