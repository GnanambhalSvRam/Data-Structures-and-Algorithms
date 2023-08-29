/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int minimum(int a, int b)
    {
        if(a<b)
            return a;
        return b;
    }

    int minDepth(TreeNode* root) 
    {
        //base case
        if(root == NULL)
            return 0;

        int left = minDepth(root->left);
        int right = minDepth(root->right);

        if(left != 0 && right != 0)
            return (1+minimum(left,right));
        
        if(left == 0)
            return(1+right);
            
        return(1+left); 
    }
};
