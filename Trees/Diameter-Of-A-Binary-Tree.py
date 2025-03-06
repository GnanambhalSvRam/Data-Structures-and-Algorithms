# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0
        
        def recurse(node):

            left, right = 0, 0

            if node.left:
                left = max(recurse(node.left)) + 1
            if node.right:
                right = max(recurse(node.right)) + 1

            length = left + right
            if length > self.result:
                self.result = length

            return (left,right)

        recurse(root)
        return self.result
