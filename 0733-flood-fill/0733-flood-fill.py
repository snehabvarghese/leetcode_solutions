from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        r=len(image)
        c=len(image[0])
        q=deque()
        visited=[row[:] for row in image]
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        q.append((sr,sc))
        visited[sr][sc]=color
        original=image[sr][sc]
        while q:
            row,col=q.popleft()
            for i in range(4):
                new_row=row+dr[i]
                new_col=col+dc[i]
                
                if new_row>=0 and new_col>=0 and new_row<r and new_col<c and original==image[new_row][new_col] and visited[new_row][new_col]!=color:
                    q.append((new_row,new_col))
                    visited[new_row][new_col]=color
        return visited


            

        