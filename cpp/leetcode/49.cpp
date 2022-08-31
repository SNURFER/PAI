#include <vector>
#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (auto str : strs) {
            priority_queue<char> order;
            for (auto ch : str) {
                order.push(ch);
            }
            string word;

            while(order.size() > 0) {
                char ch = order.top();
                order.pop();
                word.push_back(ch);
            }

            map[word].push_back(str);
        }

        vector<vector<string>> retVal;
        for (auto item : map) {
            retVal.push_back(item.second);
        }

        return retVal;
    }
};

int main() {
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};
    Solution solution;
    auto ret = solution.groupAnagrams(strs);

    return 0;
}
