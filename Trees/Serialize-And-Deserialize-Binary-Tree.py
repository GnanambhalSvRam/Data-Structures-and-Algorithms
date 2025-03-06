# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        queue = deque()
        array = []

        queue.append(root)
        while queue:
            node = queue.popleft()

            if node is None:
                array.append('N')
            else:
                array.append(str(node.val))
            array.append('.')

            if node:
                queue.append(node.left)
                queue.append(node.right)

        array.pop()
        serialized = "".join(array)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        array = data.split('.')

        queue = deque()
        val = array.pop(0)
        root = TreeNode(int(val))
        queue.append(root)

        while queue:
            node = queue.popleft()

            leftNode, rightNode = None, None
            left, right = array.pop(0), array.pop(0)

            if left != 'N':
                leftNode = TreeNode(int(left))

            if right != 'N':
                rightNode = TreeNode(int(right))

            node.left = leftNode
            node.right = rightNode

            if leftNode:
                queue.append(leftNode)
            if rightNode:
                queue.append(rightNode)

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
