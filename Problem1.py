# T.C: O(n)
# S.C: O(h) -> height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,level,result):
        if not root:
            return
        if level == len(result):
            result.append(-1)
        result[level] = root.val
        self.dfs(root.left,level+1,result)
        self.dfs(root.right,level+1,result)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        self.dfs(root,0,result)
        return result
        
