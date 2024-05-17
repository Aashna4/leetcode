''' 
Time complexity = O(n)
Space complexity = O(1)

Intuition: We use left and right pointers to get the nth element from last. Essentially we need the right pointer to tell 
us when the list has ended. Initally, we place the left and right pointers with a difference of n+1 and then
increment both by 1 till right reached the end. At this point, left will be at the n+1th position from last. Change the next
pointer to delete the nth element. 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        left = res 
        right = head
        
        while n>0 and right:
            right = right.next 
            n-=1 
        
        while right:
            left = left.next 
            right = right.next
        
        left.next = left.next.next

        return res.next
        
        