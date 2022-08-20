# https://leetcode.com/problems/same-tree/discuss/32894/Python-Recursive-solution-and-DFS-Iterative-solution-with-stack-and-BFS-Iterative-solution-with-queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree1(p, q):
    if p and q:
        return p.val == q.val and isSameTree1(p.left, q.left) and isSameTree1(p.right, q.right)
    else:
        return p == q

# DFS with stack        
def isSameTree2( p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    return True
 
# BFS with queue    
def isSameTree3(self, p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True

l = [5,1,6,0,2]
root = TreeNode()
root.val = 5
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)

l = [5,1,6,0,2]
root1 = TreeNode()
root1.val = 5
root1.left = TreeNode(1)
root1.right = TreeNode(6)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(2)


print("Ans: ", isSameTree1(root, root1))