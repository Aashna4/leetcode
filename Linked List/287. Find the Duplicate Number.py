# Time complexity: O(n)

# No extra space - using Floyd's slow and fast pointers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0 

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break 
        
        return slow

# Using extra space - set/hash table approach 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)