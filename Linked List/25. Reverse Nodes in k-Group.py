'''
Time complexit: O(nk)
Space Complexity: O(1)

Intuition: Reverse in groups of length k if possible. Keep a track of the prev and next nodes for each group 
to reverse the links of the reversed group.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = groupPrev = ListNode(0, head)

        while True:
            # print("\nprev node : ", groupPrev)
            kthNode = self.getKthNode(groupPrev, k)
            
            if not kthNode:
                break
            groupNext = kthNode.next 

            cur = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = cur
            prev = groupNext
            while cur!=kthNode:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            kthNode.next = prev

            
        
        return res.next

        
    def getKthNode(self, node, k):
        while k>0 and node:
            node = node.next
            k-=1
        return node


