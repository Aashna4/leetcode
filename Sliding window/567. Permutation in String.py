'''
Time complexity = O(n), where n is len(s2)
Space complexity = O(n)

Intuition: Create a frequency count dictionary/hash table for s1
        slide through window sizes equal to the length if s1 in s2. 
        for each window make a hash table and compar ewith s1's table 
        increment the l pointer and right pointer by 1. update the hash table for this wondow by   
        decrementing the count for char[l] and incremening the count for char[r] and then compare again. 
        repeat till r is less than the lenght of s2.  

''' 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)>len(s1):
            return False

        count_s1, count_s2 = {}

        for i in s1:
            count_s1[i] = 1 + count_s1.get(i, 0)

        l,r = 0

        while r<len(s2):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)

            if count_s1 == count_s2:
                return True
            
            if (r-l+1) == len(s1):
                count_s2[s2[l]]-=1 
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                l+=1
            
            r+=1
        
        return False
