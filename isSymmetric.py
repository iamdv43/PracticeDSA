class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
        def isSameTree(p, q):
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
            else:
                return p == q
        return isSameTree(root.left, root.right)
    
l = [1,2,2,3,4,4,3]
root = TreeNode()
root.val = 1
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


print("Ans: ", isSymmetric(root))

l = [1,2,2,None,3,None,3]
root = TreeNode()
root.val = 1
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(None)
root.left.right = TreeNode(3)
root.right.left = TreeNode(None)
root.right.right = TreeNode(3)


print("Ans: ", isSymmetric(root))