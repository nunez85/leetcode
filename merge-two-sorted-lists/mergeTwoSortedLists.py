class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return None

        c1 = list1
        c2 = list2

        newHead = ListNode(-1)
        head = newHead

        while c1 or c2:
            if c1:
                if c2:
                    if c1.val < c2.val:
                        newHead.next = ListNode(c1.val)
                        c1 = c1.next
                    else:
                        newHead.next = ListNode(c2.val)
                        c2 = c2.next
                else:
                    newHead.next = ListNode(c1.val)
                    c1 = c1.next
            else:
                newHead.next = ListNode(c2.val)
                c2 = c2.next

            newHead = newHead.next
            
        return head.next 