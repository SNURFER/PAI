#include <vector>
#include <iostream>


using namespace std;

class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        int n = nums.size();
        vector<int> targetVec;

        for (int i = 0; i < n; i++) {
            targetVec.insert(targetVec.begin() + index[i], nums[i]);
        }

        return targetVec;
    }
};

int main() {

    vector<int> nums = {0, 1, 2, 3, 4};
    vector<int> index = {0, 1, 2, 2, 1};

    Solution solution;
    auto retVal = solution.createTargetArray(nums, index);
    for (auto item : retVal) {
        cout << item << endl;


    }


    return 0;
}