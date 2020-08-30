# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #My first attempt, great run-time, but poor memory usage
    def maxDepthFirst(self, root: TreeNode) -> int:
        maxL = 0
        def depthSearch(root, n):
            nonlocal maxL
            if maxL < n:
                maxL = n
            if root.left and root.right:
                depthSearch(root.left, n+1)
                depthSearch(root.right, n+1)
            elif root.left:
                depthSearch(root.left, n+1)
            elif root.right:
                depthSearch(root.right, n+1)
            
        if root:
            depthSearch(root, 1)
        return maxL
    
    #My second attempt, goes down the tree until it reaches the bottom. Once at bottom, it goes back up each         branch and compares with the other leaf to see which one is longer.
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))