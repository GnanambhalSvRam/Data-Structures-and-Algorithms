# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilts = []

        def sum(node):
            
            sumRight, sumLeft = 0, 0

            if node.right: 
                sumRight = sum(node.right)

            if node.left:
                sumLeft = sum(node.left)

            self.tilts.append(abs(sumRight-sumLeft))

            return node.val + sumRight + sumLeft

        rootSum = sum(root)
        return sum(self.tilts)
