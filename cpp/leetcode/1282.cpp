#include <vector>
#include <map>
#include <iostream>

class Solution {
public:
    std::vector<std::vector<int>> groupThePeople(std::vector<int>& groupSizes) {
        std::vector<std::vector<int>> retVal;
        std::map<int, std::vector<int>> groupMap;
        for (size_t i = 0; i < groupSizes.size(); i++) {
            groupMap[groupSizes[i]].push_back(i);
        }
        for (auto item : groupMap) {
            int num = item.first;
            int len = item.second.size();
            std::vector<int> people = item.second;

            for (int i = 0; i < (len / num); i++) {
                std::vector<int> smallGroup;
                for (int j = 0; j < num; j++) {
                    smallGroup.push_back(people[(num * i) + j]);
                }
                retVal.push_back(smallGroup);
            }
        }
        return retVal;
    }
};

int main() {
//    std::vector<int> input = {2,1,3,3,3,2};
    std::vector<int> input = {2,2,1,1,1,1,1,1};
    Solution solution;
    auto output = solution.groupThePeople(input);
    for (auto row : output) {
        for (auto col : row) {
            std::cout << col << std::endl;
        }
    }


    return 0;
}
