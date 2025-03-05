# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversal(node) -> list:

            result = []
            def recurse(node):
                if node is None:
                    result.append('#')
                    return

                result.append(node.val)
                recurse(node.left)
                recurse(node.right)

            recurse(node)
            return result

        tree1 = traversal(p)
        tree2 = traversal(q)

        return tree1 == tree2
