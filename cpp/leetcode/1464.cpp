#include <vector>
#include <queue>
#include <iostream>

using namespace std;


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int> pq;
        for (const auto& num : nums) {
            pq.push(num);
        }

        int topOne = pq.top();
        pq.pop();
        int topTwo = pq.top();
        pq.pop();

        return (topOne - 1) * (topTwo - 1);
    }
};

int main() {
    vector<int> nums = { 3, 4, 5, 2 };
    Solution solution;
    cout << solution.maxProduct(nums) << endl;

    return 0;
}
