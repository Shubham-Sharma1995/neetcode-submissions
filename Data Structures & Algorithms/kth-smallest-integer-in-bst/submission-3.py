# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stack=[] #doing iteratively
        pointerCurr=root #what node we are currently visiting or currently at

        while pointerCurr or stack:
            while pointerCurr:
                stack.append(pointerCurr)
                pointerCurr=pointerCurr.left
            pointerCurr=stack.pop()
            n +=1
            if n == k:
                return pointerCurr.val
            pointerCurr=pointerCurr.right











        