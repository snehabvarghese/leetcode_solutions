class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        arr=[[-1]*2 for _ in range(n)]
        def dfs(i,buying):
            if i>=n:
                return 0
            if arr[i][buying]!=-1:
                return arr[i][buying]
            if buying:
                buy=-prices[i]+dfs(i+1,0)
                skip=dfs(i+1,1)
                arr[i][buying]=max(buy,skip)
            else:
                sell=prices[i]+dfs(i+2,1)
                hold=dfs(i+1,0)
                arr[i][buying]=max(sell,hold)
            return arr[i][buying]
        return dfs(0,1)



