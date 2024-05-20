'''
Time Complexity = O(n)
Space Complexity = O(n)

Intuition: the digits are reversed already, so we only need to add the corresponding nodes and carry if present. 

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = sumList = ListNode()
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum>9:
                sum = sum%10 
                carry = 1
            else:
                carry = 0
            sumList.next = ListNode(sum)
            sumList = sumList.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            if sum>9:
                sum = sum%10 
                carry = 1
            else:
                carry = 0
            sumList.next = ListNode(sum)
            sumList = sumList.next
            l1 = l1.next
        
        while l2:
            sum = l2.val + carry
            if sum>9:
                sum = sum%10 
                carry = 1
            else:
                carry = 0
            sumList.next = ListNode(sum)
            sumList = sumList.next
            l2 = l2.next
        
        if carry!=0:
            sumList.next = ListNode(carry)
            

        return res.next

        


