#include <string>
#include <iostream>

class Solution {
public:
    int maxDepth(std::string s) {
        for (auto& ch : s) {
            std::cout << ch << std::endl;
        }

        return 0;
    }
};

int main() {
    std::string s = "(1)+((2))+(((3)))";
    Solution solution;
    solution.maxDepth(s);

    return 0;
}
