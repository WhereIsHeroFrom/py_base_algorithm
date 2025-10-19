# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, a, b):
        a = self.sortList(a)
        b = self.sortList(b)
        head = ListNode()
        tail = head
        while a or b:
            if a == None:
                tail.next = b
                break
            elif b == None:
                tail.next = a
                break
            elif a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
            tail.next = None
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        fast = head
        slow = head
        prev = None
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        # head -> ... -> prev 
        # slow -> ... -> fast(None)
        prev.next = None
        return self.mergeSort(head, slow)