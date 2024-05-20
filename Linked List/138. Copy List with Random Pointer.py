'''
Time Complexity = O(n)
Space Complexity = O(n)

Intuition: To make a deep copy with random pointers we need those nodes to be defined before we can define the random pointers. Hence,
we need to make two passes through the linked list. in the first pass, we create a hash map mapping the old original nodes to the 
new copy nodes and initialise just the values. In the second pass, using the hashmap we initialise the next and random poinetrs 
for the deep copy. 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy = { None : None }

        cur = head 
        while cur:
            copy = Node(cur.val)
            deepCopy[cur] = copy
            cur = cur.next 

        cur = head
        while cur:
            copy = deepCopy[cur]
            copy.next = deepCopy[cur.next]
            copy.random = deepCopy[cur.random]
            cur = cur.next
        
        return deepCopy[head]

        