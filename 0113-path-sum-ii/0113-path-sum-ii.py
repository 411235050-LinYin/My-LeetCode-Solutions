# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # 1. 將當前節點加入路徑
            path.append(node.val)
            current_sum -= node.val
            
            # 2. 判斷是否為葉子節點，且總和剛好為 0
            if not node.left and not node.right and current_sum == 0:
                res.append(list(path)) # 注意：要用 list(path) 複製一份複本
            
            # 3. 遞迴左右子樹
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            
            # 4. 回溯：把最後加入的節點彈出，回到上一層
            path.pop()
            
        dfs(root, targetSum, [])
        return res
        