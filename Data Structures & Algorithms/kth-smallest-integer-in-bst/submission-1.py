# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, node, res):
        if node is None:
            return 
        self.inOrder(node.left, res)
        res.append(node.val)
        self.inOrder(node.right, res)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.inOrder(root, nodes)
        return nodes[k-1]
        