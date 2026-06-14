class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_price = prices[0]
        max_profit = 0

        for i in range(0,len(prices)):
            s_price = prices[i]
            
            if s_price > b_price:
                profit = s_price - b_price
                max_profit = max(max_profit, profit)
            b_price = min(b_price,s_price)
        return max_profit