# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Iterative Solution
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head #setting node currently on
            head = head.next #iterating the linked list for next loop
            curr.next = prev #setting the link from current node to previous node
            prev = curr #updating previous to be current for the next iteration
        return prev
    
    #Recursive Solution
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p = reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        