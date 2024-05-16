'''
Time complexity = O(n)
Space complexity = O(1)

Intuition: Use two pointers to keep track of the minimum value on the left and maximum value on the 
right for maximum difference (profit)
'''    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        for i in range(0, len(prices)):
            right = i
            if prices[i]<prices[left]:
                left = i
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        
        return max_profit
    
'''
Input:
prices =
[7,1,5,3,6,4]

Output:
5

Input: 
prices =
[7,6,4,3,1]

Output:
0
'''