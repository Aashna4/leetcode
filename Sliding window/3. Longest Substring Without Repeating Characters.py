'''
Time complexity = O(n) - eachc haracter is visited at most twice 
Space complexity = O(n)

Intuition: At each point l and r are end points of the substring. If a duplicate character occurs, 
we move the left pointer to the next character. We keep on doing so until that character is not present in the substring. 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len