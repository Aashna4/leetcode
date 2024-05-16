'''
Time complexity = O(m+n), where m=len(s) and n=len(t)
Space complexity = O(1), max size of dictionaries used will be 26 (number of alphabets)

Intuition: Make a dictioanry with the count of characters in t string. We need to find a window in s with the least size such that it
contains all the characters of t. Move the right pointer till we get a window which has all the characters of t. Once we have a 
valid window, move the left pointer to remove the unwanted leading characters to get the smallest window.
'''    

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT, window = {}, {}

        if len(s) < len(t):
            return ""
        
        if t == "":
            return ""

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        have, need = 0, len(t)
        l = 0
        res = [0, 0]
        reslen = r-l+1

        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if window[ch] == countT[ch]:
                have+=1 

            while have == need:

                if r-l+1 < reslen:
                    res = [l, r]
                    reslen = r-l+1
                
                window[s[l]]-=1
                if window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1

        l, r = res
        return s[l:r+1] if reslen!=float("infinity") else ""