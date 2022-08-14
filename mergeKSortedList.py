class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l, r = mergeKLists(lists[:mid]), mergeKLists(lists[mid:])
    return merge(l, r)
    
def merge(l, r):
    dummy = p = ListNode()
    while l and r:
        if l.val < r.val:
            p.next = l
            l = l.next
        else:
            p.next = r
            r = r.next
        p = p.next
    p.next = l or r
    return dummy.next

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
l = [1,3,4]
l3 = node = ListNode(0)
for i in l:
    node.next = ListNode(i)
    node = node.next
lists = [l1.next, l2.next, l3.next]
ans = mergeKLists(lists)
print(ans)