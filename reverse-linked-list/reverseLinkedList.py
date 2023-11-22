
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    if not head:
        return head

    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    newHead = ListNode(stack.pop())
    cur = newHead
    while stack:
        cur.next = ListNode(stack.pop())
        cur = cur.next
    
    return newHead
    