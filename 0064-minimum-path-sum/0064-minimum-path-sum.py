class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        c=len(grid[0])
        r=len(grid)
        arr=[[0]*c for _ in range(r)]
        arr[0][0]=grid[0][0]
        for i in range(1,r):
            arr[i][0]=grid[i][0]+arr[i-1][0]
        for j in range(1,c):
            arr[0][j]=grid[0][j]+arr[0][j-1]
        for i in range(1,r):
            for j in range(1,c):
                arr[i][j]=grid[i][j]+min(arr[i][j-1],arr[i-1][j])
        return arr[-1][-1]