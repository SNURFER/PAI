#include <iostream>
#include <stack>
#include <algorithm>

class Solution {
public:
    int maxDepth(std::string s) {
        std::stack<char> chStack;

        int depthCount = 0;
        int maxCount = 0;

        for (auto& ch : s) {
            if (ch == '(') {
                chStack.push(ch);
                depthCount += 1;
                maxCount = std::max(maxCount, depthCount);
            } else if (ch == ')') {
                depthCount -= 1;
                chStack.pop();
            }
        }

        return maxCount;
    }
};

int main() {
    std::string s = "(1)+((2))+(((3)))";
    Solution solution;
    std::cout << solution.maxDepth(s) << std::endl;

    return 0;
}
