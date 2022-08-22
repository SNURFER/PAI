#include <iostream>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        queue<TreeNode*> numQueue;
        numQueue.push(root);

        int depthSum = 0;
        while (numQueue.size() > 0) {
            depthSum = 0;
            size_t n = numQueue.size();

            for (size_t i = 0; i < n; i++) {
                TreeNode* node = numQueue.front();
                numQueue.pop();
                depthSum += node->val;

                if (node->left) numQueue.push(node->left);
                if (node->right) numQueue.push(node->right);
            }
        }
        return depthSum;
    }
};

int main() {
//    root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    TreeNode node8 = TreeNode(8);
    TreeNode node7 = TreeNode(7);
    TreeNode node6 = TreeNode(6, nullptr, &node8);
    TreeNode node5 = TreeNode(5);
    TreeNode node4 = TreeNode(4, &node7, nullptr);
    TreeNode node3 = TreeNode(3, nullptr, &node6);
    TreeNode node2 = TreeNode(2, &node4, &node5);
    TreeNode node1 = TreeNode(1, &node2, &node3);
    Solution solution;

    int ans = solution.deepestLeavesSum(&node1);
    cout << ans << endl;


    return 0;
}