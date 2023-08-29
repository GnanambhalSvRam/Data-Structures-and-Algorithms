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
class Solution 
{
public:
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        if(root == NULL)
            return {};

        queue<pair<TreeNode*,int>> q;
        vector<vector<int>> res;
        q.push({root,0});

        while(!q.empty())
        {
            pair temp = q.front();
            int index = temp.second;
            TreeNode *ptr = temp.first;
            q.pop();
            
            if(res.size()<index+1)
                res.push_back({});
            
            if(ptr!=NULL)
                res[index].push_back(ptr->val);
            if(ptr->left != NULL)
                q.push({ptr->left,index+1});
            if(ptr->right != NULL)
                q.push({ptr->right,index+1});
        }

        return res;
    }
};
