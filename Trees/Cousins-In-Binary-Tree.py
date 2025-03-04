# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        depth, parents = [], []
        queue = deque()
        queue.append((root,0))

        while queue:
            
            length = len(queue)
            for _ in range(length):
                node,level = queue.popleft()
                if node.left is not None:
                    queue.append((node.left,level+1))
                    if node.left.val in (x,y):
                        depth.append(level)
                        parents.append(node)
                if node.right is not None:
                    queue.append((node.right,level+1))
                    if node.right.val in (x,y):
                        depth.append(level)
                        parents.append(node)

        if len(depth) == 2 and depth[0] == depth[1] and parents[0] != parents[1]:
            return True

        return False
