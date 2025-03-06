# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        self.maxVal = root.val

        def recurse(node):

            left,right = 0,0

            if node.left:
                left = max(max(recurse(node.left)) + node.left.val, 0)
            if node.right:
                right = max(max(recurse(node.right)) + node.right.val, 0)

            self.maxVal = max(self.maxVal, node.val, left + node.val, node.val + right, left + node.val + right)

            return (left,right)

        recurse(root)
        return self.maxVal
