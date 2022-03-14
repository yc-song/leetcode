#include<iostream>
#include<vector>
#include <algorithm>
#include <cstdlib>

class Solution {
public:
    bool isBalanced(TreeNode* curnode) {
        if (curnode!= nullptr) {
            if(traversal(curnode) == false) return false;
        if (curnode->left != nullptr) {
            if(isBalanced(curnode->left)==false) return false;}
        if (curnode->right != nullptr) {
            if(isBalanced(curnode->right)==false) return false;}
        }        return true;
}
    bool traversal(TreeNode* curnode) {
        int x;
        int y;
        if (curnode->left != nullptr) x = __traversal(curnode->left, 1);
        else x =0;
        if (curnode->right != nullptr) y = __traversal(curnode->right, 1);
        else y=0;        
        // std::cout<<"curnode->val "<<curnode->val<<std::endl;
        // std::cout<<"x "<<x<<std::endl;
        // std::cout<<"y "<<y<<std::endl;

        if (abs(x - y) > 1) return false;
        else return true;
           
    }
       
    
//private:
    int __traversal(TreeNode* curnode, int height) {
        if (curnode->left != nullptr && curnode->right != nullptr) {
            height++;
            int x = __traversal(curnode->left, height);
            int y = __traversal(curnode->right, height);
            return(std::max(x, y));

        }

        else if (curnode->left != nullptr && curnode->right == nullptr) return __traversal(curnode->left, ++height);
        else if (curnode->left == nullptr && curnode->right != nullptr) return __traversal(curnode->right, ++height);
        else return height;

    }

};