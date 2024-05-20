'''
Time Complexity = O(n)
Space Complecity = O(n) (hashmap)
                   O(1) (Floyd's) 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using a hashmap 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        track = {}

        while cur:
            if cur in track:
                return True
            track[cur] = True 
            cur = cur.next
        
        return False

# Using Floyd's tortise and Hare 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                return True 
        
        return False
        