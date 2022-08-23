#include <vector>
#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> nums;
        ListNode* slowWalker = head;
        ListNode* fastWalker = head;
        while (fastWalker != nullptr) {
            nums.push_back(slowWalker->val);

            slowWalker = slowWalker->next;
            fastWalker = fastWalker->next->next;
        }

        int n = nums.size() - 1;
        while (slowWalker != nullptr) {
            nums[n] += slowWalker->val;
            n -= 1;
            slowWalker = slowWalker->next;
        }

        sort(nums.begin(), nums.end());

        return nums[nums.size() - 1];
    }
};

int main() {
    ListNode node4(1);
    ListNode node3(2, &node4);
    ListNode node2(4, &node3);
    ListNode node1(5, &node2);
    Solution solution;
    cout << solution.pairSum(&node1) << endl;

    return 0;
}
