#include <iostream>
#include <vector>

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
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> elemContainer;

        dfs(root1, elemContainer);
        dfs(root2, elemContainer);

        sort(elemContainer.begin(), elemContainer.end());

        for (auto elem : elemContainer) {
            cout << elem << endl;
        }

        return elemContainer;
    }

    void dfs(TreeNode* node, vector<int>& elementContainer) {
        if (node == nullptr) return;

        elementContainer.push_back(node->val);

        dfs(node->left, elementContainer);
        dfs(node->right, elementContainer);
    }
};

int main() {
    TreeNode node1(1);
    TreeNode node2(2);
    TreeNode node3(3);
    node1.left = &node2;
    node1.right = &node3;


    TreeNode node4(1);
    TreeNode node5(4);
    TreeNode node6(6);
    node4.left = &node5;
    node4.right = &node6;

    Solution solution;
    solution.getAllElements(&node1, &node4);

    return 0;
}
