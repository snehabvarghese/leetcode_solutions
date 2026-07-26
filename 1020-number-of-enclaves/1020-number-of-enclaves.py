class Solution(object):
    def dfs(self,i,j,grid,visited):
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        visited[i][j]=1
        for k in range(4):
            new_r=i+dr[k]
            new_c=j+dc[k]
            if new_c>=0 and new_c<len(grid[0]) and new_r>=0 and new_r<len(grid ) and grid[new_r][new_c]==1 and visited[new_r][new_c]==0:
                self.dfs(new_r,new_c,grid,visited)
    def numEnclaves(self, grid):
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            if grid[r][0]==1:
                self.dfs(r,0,grid,visited)
            if grid[r][len(grid[0])-1]==1:
                self.dfs(r,len(grid[0])-1,grid,visited)
        for c in range(len(grid[0])):
            if grid[0][c]==1:
                self.dfs(0,c,grid,visited)
            if grid[len(grid)-1][c]==1:
                self.dfs(len(grid)-1,c,grid,visited)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==0:
                    count+=1
        return count