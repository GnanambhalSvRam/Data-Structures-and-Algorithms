# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        if root.left is None and root.right is None:
            return root.val
        
        self.array = []
        
        def inorder(node):

            if node is None:
                return

            inorder(node.left)
            self.array.append(node.val)
            inorder(node.right)

            return
        
        inorder(root)

        minDiff = float('inf')
        for i in range(1,len(self.array)):
            diff = self.array[i] - self.array[i-1]
            if diff < minDiff:
                minDiff = diff

        return minDiff
