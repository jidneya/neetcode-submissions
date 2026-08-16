# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        path1 = [current]
        while current.val != p.val:
            if current.val > p.val:
                current = current.left
            else:
                current = current.right
            path1.append(current)

        current = root
        path2 = [current]
        while current.val != q.val:
            if current.val > q.val:
                current = current.left
            else:
                current = current.right
            path2.append(current)

        res = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                res = path1[i]
            else:
                break
        return res
        
        

        