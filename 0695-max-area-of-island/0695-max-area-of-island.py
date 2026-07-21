class Solution(object):
    def dfs(self,grid,row,col):
        count=1
        grid[row][col]=0
        lst=[(row,col+1),(row,col-1),(row+1,col),(row-1,col)]
        for r,c in lst:
            if r>=0 and c>=0 and r< len(grid) and c< len(grid[0]) and grid[r][c]==1:
                count+=self.dfs(grid,r,c)
                
        return count



    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    res=max(res,self.dfs(grid,r,c))
        return res