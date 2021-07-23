# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0,0
            l1,l = dfs(root.left)
            r1,r = dfs(root.right)
            print(r1,r, l1, l)
            return (root.val + l +r,max(l,l1) + max(r,r1))
        
        return max(dfs(root))
    
