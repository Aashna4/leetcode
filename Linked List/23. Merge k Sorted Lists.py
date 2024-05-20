'''
Time complexity = O(nlogk)

Intuition: Similar to merge sort, we merge lists in pairs till we get one merged list. 
merge2lists is a basic function to merge two linked lists. 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None

                mergedLists.append(self.merge2lists(l1, l2))
               
            lists = mergedLists

        return lists[0]

    def merge2lists(self, l1, l2):
        res = temp = ListNode()

        while l1 and l2:
            if l1.val<l2.val:
                temp.next = l1
                l1 = l1.next 
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1
        
        if l2:
            temp.next = l2

        return res.next        
            