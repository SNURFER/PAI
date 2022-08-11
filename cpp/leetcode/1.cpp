
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
    map<int, int> numMap;
    vector<int> output;

    int n = nums.size();
    for (int i = 0; i < n; i++) {
        numMap[nums[i]] = i; 
    }

    for (int i = 0; i < n; i++) {
        if (numMap.find(target - nums[i]) != numMap.end() && 
            numMap[target - nums[i]] != i) {
                output.push_back(i);
                output.push_back(numMap[target - nums[i]]);
                break;
            }
    }
    return output;

}

int main() {

    vector<int> input = {2, 7, 11, 15};
    int target = 22;

    vector<int> output = twoSum(input, target);

    for (auto i : output) {
        cout << i << endl;
    }
    

    return 0;
}