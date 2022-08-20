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
private:
    int sumVal;
public:
    Solution(): sumVal(0) {}
    int sumEvenGrandparent(TreeNode* root) {

        dfs(root, nullptr, false);

        return this->sumVal;
    }
    void dfs(TreeNode* targetNode, TreeNode* parentNode, bool isGrandEven) {
        if (targetNode == nullptr) return;

        if (isGrandEven) {
            cout << this->sumVal << endl;
            this->sumVal += targetNode->val;
        }

        // if parent node is even child val need to be calculated
        if (parentNode && parentNode->val % 2 == 0) {
            dfs(targetNode->left, targetNode, true);
            dfs(targetNode->right, targetNode, true);
        } else {
            dfs(targetNode->left, targetNode, false);
            dfs(targetNode->right, targetNode, false);
        }

    }
};

int main() {
//    root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    TreeNode node9(5);
    TreeNode node8(9);
    TreeNode node7(3, nullptr, &node9);
    TreeNode node6(1);
    TreeNode node5(7);
    TreeNode node4(2, &node8, nullptr);
    TreeNode node3(8, &node6, &node7);
    TreeNode node2(7, &node4, &node5);
    TreeNode node1(6, &node2, &node3);

    Solution solution;
    cout << solution.sumEvenGrandparent(&node1) << endl;


    return 0;
}