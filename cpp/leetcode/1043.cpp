#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;
// hard to understand..

class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n + 1, 0);

        for (int i = 1; i < n + 1; i++) {
            int maxInSub = 0;
            int sumMaxInSub = 0;
            for (int j = 1; i >= j && j <= k; j++) {
                maxInSub = max(maxInSub, arr[i - j]);
                sumMaxInSub = max(sumMaxInSub, dp[i - j] + maxInSub * j);
            }
            dp[i] = sumMaxInSub;
        }
        return dp[n];
    }
};


int main() {

    vector<int> arr = {1,15,7,9,2,5,10};
    int k = 3;

    Solution solution;
    cout << solution.maxSumAfterPartitioning(arr, k) << endl;

}