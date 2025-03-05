# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0 

        self.total = 0

        def binary(node, elements: list):

            if node.left:
                elements.append(str(node.left.val))
                binary(node.left, elements)
                elements.pop()

            if node.right:
                elements.append(str(node.right.val))
                binary(node.right, elements)
                elements.pop()

            if node.left is None and node.right is None:
                self.total = self.total + int("".join(elements),2)
                
            return

        binary(root,[str(root.val)])
        return self.total
