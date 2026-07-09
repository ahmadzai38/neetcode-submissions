# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxSeen):
            if not node:
                return 0
            if node.val >= maxSeen:
                good = 1
            else:
                good = 0
            maxSeen = max(maxSeen, node.val)
            return good + dfs(node.left,maxSeen) + dfs(node.right,maxSeen)
        return dfs(root,float('-inf'))