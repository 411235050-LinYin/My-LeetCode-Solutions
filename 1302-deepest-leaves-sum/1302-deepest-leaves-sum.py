# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.total = 0
        
        def dfs(node, depth):
            if not node: return
            
            if depth > self.max_d:
                self.max_d = depth
                self.total = node.val
            elif depth == self.max_d:
                self.total += node.val
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return self.total
        