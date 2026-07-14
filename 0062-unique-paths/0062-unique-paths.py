class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for i in range(m)]
        # [
        #  [1,1,1,1,1,1,1],
        #  [1,2,3,4,5,6,7],
        #  [1,3,6,10,15,21,28]
        # ]
        for i in range(n):
            dp[0][i]=1
        for j in range(m):
            dp[j][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        
    