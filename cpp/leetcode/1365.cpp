#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sortNums = nums;
        vector<int> retNums;
        std::sort(sortNums.begin(), sortNums.end());

        for (const auto& num : nums) {
            int count = 0;
            for (const auto& sortNum : sortNums) {
                if (sortNum >= num) {
                    break;
                }
                count += 1;
            }
            retNums.push_back(count);
        }
        return retNums;

    }
};

int main() {

    vector<int> nums = {8,1,2,2,3};
    Solution solution;
    vector<int> retVal = solution.smallerNumbersThanCurrent(nums);
    for (auto val : retVal) {
        cout << val << endl;
    }

    return 0;
}