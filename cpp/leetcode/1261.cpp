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

class FindElements {
private:
    TreeNode* m_node;
public:
    FindElements(TreeNode* root) {
        m_node = root;
    }

    bool correctAndFind(TreeNode* node, int target) {
        if (node->val == target) return true;
        bool leftFound = false;
        bool rightFound = false;
        if (node->left != nullptr) {
            node->left->val = 2 * node->val + 1;
            leftFound = correctAndFind(node->left, target);
        }
        if (node->right != nullptr) {
            node->right->val = 2 * node->val + 2;
            rightFound = correctAndFind(node->right, target);
        }
        return leftFound || rightFound;
    }

    bool find(int target) {
        m_node->val = 0;
        return correctAndFind(m_node, target);

    }
};


int main() {
    TreeNode node6(1);
    TreeNode node5(1, nullptr, &node6);
    TreeNode node4(1);
    TreeNode node3(1, &node4, &node5);
    TreeNode node2(1);
    TreeNode node1(1, &node2, &node3);

    FindElements* obj = new FindElements(&node1);
    bool param_1 = obj->find(6);
    cout << param_1 << endl;

    return 0;
}