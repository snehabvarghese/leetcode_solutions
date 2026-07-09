
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        def sol(i,j):
            if i==0 or j==0:
                return 1
            else:
                if dp[i][j]==0:
                    dp[i][j]=(sol(i-1,j)+sol(i,j-1))
                return dp[i][j]
        return sol(m-1,n-1)

        