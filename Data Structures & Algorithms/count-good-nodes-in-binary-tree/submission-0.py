# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, maxValue):
            if not root:
                return 0
            
            res = 0
            if root.val >= maxValue:
                res = 1
            maxValue = max(maxValue, root.val)
            res+= traverse(root.left, maxValue) + traverse(root.right, maxValue)
            return res
        return traverse(root, root.val) 
        