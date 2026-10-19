class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        memo={}
        def f(idx,buy):
            if idx>=n:
                return 0
            if (idx,buy) in memo:
                return memo[(idx,buy)]
            if buy:
                profit=max((-prices[idx]+f(idx+1,0)),
                           f(idx+1,1))
                
            else: 
                profit=max(prices[idx]+f(idx+2,1),
                           f(idx+1,0))
            memo[(idx,buy)]=profit
            return profit
        return f(0,1)