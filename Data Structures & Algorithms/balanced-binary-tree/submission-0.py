# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0
            #check left subtree

            left_height=dfs(curr.left)
            if left_height==-1:
                return -1 #unbalanced flow
            right_height = dfs(curr.right)
            if right_height == -1: 
                return -1  # Already unbalanced below
            if abs(left_height- right_height)>1:
                return -1
            return max(left_height,right_height)+1


        return dfs(root) != -1

            

        