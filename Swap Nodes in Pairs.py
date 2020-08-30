# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Recursive Solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def pairSwap(node):
            if node is None or node.next is None:
                return
            if node.next:
                pairSwap(node.next.next)
                node.val, node.next.val = node.next.val, node.val
        pairSwap(head)
        return head
        