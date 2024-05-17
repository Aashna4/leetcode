'''
Time Complexity: O(n)
Space Complexity: O(1)

Intuition: Find the mid of the linked list and then reverse the second half of the list. Then merge both the lists.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        mid = ListNode()
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # reversing the seond hald of the list 

        cur = slow.next 
        prev = slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp 
            
        head2 = prev 
        head1 = head 

        while head2:
            temp1 = head1.next
            temp2 = head2.next
            head2.next = temp1
            head1.next = head2 

            head1 = temp1
            head2 = temp2
            
