class Solution {
public:
   
    int kthSmallest(TreeNode* root, int k) {
        __inorder(root,k);
        return this->x;
    }
private:

    void __inorder(TreeNode* curnode, int k) {
            if (curnode != nullptr && count <= k) {
                __inorder(curnode->left, k);
                visit(curnode, k); 
                __inorder(curnode->right, k);

            }
        

    }

    void visit(TreeNode* curnode, int k) {
        if (count < k) {
            count++;
        }
        else if (count == k) {
            this->x = curnode->val;
            count++;
        };
      
    }
     int count = 1;
    int x ;
};