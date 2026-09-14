class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_p = 0  
        
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r  # Move left pointer to the new lowest price
            r += 1  # Always advance the right pointer to prevent infinite loop
            
        return max_p
