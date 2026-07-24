from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        count=0
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        q=deque()
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    visited[i][j]=2
                    q.append((i,j,0))
        while q:
            r1,c1,ct=q.popleft()
            #t,r,b,l
            
            count=max(count,ct)
            dr=[-1,0,1,0]
            dc=[0,1,0,-1]
            for i in range(4):
                new_row=r1+dr[i]
                new_col=c1+dc[i]
                if new_row>=0 and new_col>=0 and new_row < r and new_col<c and grid[new_row][new_col]==1 and visited[new_row][new_col]!=2:
                    q.append((new_row,new_col,ct+1))
                    visited[new_row][new_col]=2
         
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and visited[i][j]!=2:
                    return -1
        return count
            
        




        

        
        