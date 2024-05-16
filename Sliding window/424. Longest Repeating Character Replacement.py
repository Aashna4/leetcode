'''
Time complexity = O(n)
Space complexity = O(1)

Intuition: Keep a count of frequency of each character in a window. 
Calculate the replacement cost. If it is greater than k, shift the window.
'''    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash map to store the frequency of characters in the current window 
        char_cnt = {}  
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1
            max_freq = max(max_freq, char_cnt[s[right]])

            if (right-left+1) - max_freq > k:
                # Shift the left pointer and decrement the counter for the char at left (shifting the window)
                char_cnt[s[left]]-=1
                left+=1
                continue

            result = max(result, (right-left+1))

        return result
            
                
