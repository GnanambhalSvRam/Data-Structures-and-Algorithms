# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None or subRoot is None:
            return False

        def traversal(root) -> list:

            array = []
            def recurse(node):
                if node is None:
                    array.append('*')
                    return

                array.append(node.val)
                recurse(node.left)
                recurse(node.right)
            recurse(root)
            return array

        mainTree = traversal(root)
        subTree = traversal(subRoot)

        for i in range(len(mainTree)):
            if mainTree[i] == subTree[0]:
                j = i + len(subTree)
                if j <= len(mainTree) and mainTree[i:j] == subTree:
                    return True

        return False
