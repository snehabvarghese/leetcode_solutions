class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        memo={}
        def f(idx,buy,cap):
            if idx==n:
                return 0
            if cap==0:
                return 0
            if (idx,buy,cap) in memo:
                return memo[(idx,buy,cap)]
            if buy:
                profit=max((-prices[idx]+f(idx+1,0,cap)),f(idx+1,1,cap))
                

            else:
                profit=max((prices[idx]+f(idx+1,1,cap-1)),f(idx+1,0,cap))
            memo[(idx,buy,cap)]=profit
            return profit
        return f(0,1,2)
