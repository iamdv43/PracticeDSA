class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                temp = l2.next
                cur.next.next = nxt
                l2 = temp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

sol = Solution()
l = [1,3,5]
l1 = node = ListNode(0)
for i in l:
    node.next = ListNode(i)
    node = node.next
l = [2,4,6]
l2 = node = ListNode(0)
for i in l:
    node.next = ListNode(i)
    node = node.next
ans = sol.mergeTwoLists(l1.next, l2.next)
print(ans)



