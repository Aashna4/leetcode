'''
Time complexity = O(n)
Space complexity = O(n)

Intuition: Using a queue which will store only the maximum values' indexes. The front of the queue will be the
maximum alue for the current window. Move the right pointer and apend the index to the queue and remove
all the values lesser than the one at right pointer from the queue. When the window size is equal to k,
move the left pointer and if the index at the front of the queue is less than left, remove it. 

'''    

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l,r = 0

        while r<len(nums):

            while q and q[nums[-1]]<nums[r] :
                q.pop()
            q.append(r)

            if l>q[0] :
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1

        return res

