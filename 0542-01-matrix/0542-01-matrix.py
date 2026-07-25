from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        dist=[[0]*len(mat[0]) for _ in range(len(mat))]
        visited=[[0]*len(mat[0]) for _ in range(len(mat))]
        q=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited[i][j]=1
        while q:
            r,c,count=q.popleft()
            dr=[-1,0,1,0]
            dc=[0,1,0,-1]
            
            
            for i in range(4):
                new_r=r+dr[i]
                new_c=c+dc[i]
                if new_r>=0 and new_c>=0 and new_r <len(mat) and new_c<len(mat[0]) and mat[new_r][new_c]==1 and visited[new_r][new_c]==0:
                    visited[new_r][new_c]=1
                    q.append((new_r,new_c,count+1))
                    dist[new_r][new_c]=count+1
        return dist
                    



        
        