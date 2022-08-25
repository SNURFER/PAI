#include <iostream>

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
    bool evaluateTree(TreeNode* root) {
        int val = root->val;

        if (val > 1) {
            bool left = evaluateTree(root->left);
            bool right = evaluateTree(root->right);
            if (val == 2) {
                return left || right;
            } else {
                return left && right;
            }
        } else {
            return val;
        }
    }
};

int main() {
//    root = [2,1,3,null,null,0,1]

    TreeNode node5(1);
    TreeNode node4(0);
    TreeNode node3(3, &node4, &node5);
    TreeNode node2(1);
    TreeNode node1(2, &node2, &node3);

    Solution solution;
    cout << solution.evaluateTree(&node1) << endl;



    return 0;
}
