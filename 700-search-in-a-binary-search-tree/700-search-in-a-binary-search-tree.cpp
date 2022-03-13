
#include <iostream>
#include <vector>

 
 class Solution {
  public:
      TreeNode* searchBST(TreeNode* root, int val) {
          TreeNode* ans = new TreeNode;
          if (root == nullptr) {
              ans = nullptr;
              return ans;
          }
          else {
              if (root->val == val) {
                 *ans = TreeNode(val, root->left, root->right);
        
              }
              else if (root->val < val) {
                  return searchBST(root->right, val);
              }
              else if (root->val > val) {
                  return searchBST(root->left, val);
              }
              return ans;
          }
      }
  };