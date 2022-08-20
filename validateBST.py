class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root, lo=float('-inf'), hi=float('inf')):
        if not root:
            return True

        if not lo < root.val < hi:
            return False
        
        return self.isValidBST(root.left, lo, min(root.val, hi)) and \
               self.isValidBST(root.right, max(lo, root.val), hi)

l = [5,1,6,0,2]
root = TreeNode()
root.val = 5
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)

    
sol = Solution()
print("Ans: ", sol.isValidBST(root))
    
