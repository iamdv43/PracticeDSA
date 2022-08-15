class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def length(self, curr):
        l = 1
        while curr.next is not None:
            l += 1
            curr = curr.next
        return curr, l

    def rotateRight(self, head, k):
        if(head is None):
            return None
        curr = head
        curr, l = self.length(curr)
        k %= l
        curr.next = head
        for i in range(l - k): 
            curr = curr.next
        head = curr.next
        curr.next = None
        return head


sol = Solution()
l = [0,1,2]
K = 4
l1 = node = ListNode(0)
for i in l:
    node.next = ListNode(i)
    node = node.next
ans = sol.rotateRight(l1.next, K)
print(ans)