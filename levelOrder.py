from pickle import NONE


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    ret = []

    level = [root]

    while root and level:
        currentNodes = []
        nextLevel = []
        for node in level:
            currentNodes.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        ret.append(currentNodes)
        level = nextLevel


    return ret

l = [3,9,20,None,None,15,7]
root = TreeNode()
root.val = 3
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print("Ans: ", levelOrder(root))