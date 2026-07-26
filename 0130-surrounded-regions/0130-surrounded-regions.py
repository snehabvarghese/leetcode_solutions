class Solution(object):
    def dfs(self,i,j,board,visited):
        visited[i][j]=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for k in range(4):
            new_r=i+dr[k]
            new_c=j+dc[k]
            if new_r>=0 and new_c>=0 and new_r<len(board) and new_c<len(board[0]) and board[new_r][new_c]=="O" and visited[new_r][new_c]==0:
                self.dfs(new_r,new_c,board,visited)
    def solve(self, board):
        if not board or not board[0]:
            return
        visited=[[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            
                
            if board[i][0]=="O":
                self.dfs(i,0,board,visited)
                
            if board[i][len(board[0])-1]=="O":
                self.dfs(i,len(board[0])-1,board,visited)
        for j in range(len(board[0])):
            if board[0][j]=="O":
                    self.dfs(0,j,board,visited)
            if board[len(board)-1][j]=="O":
                    self.dfs(len(board)-1,j,board,visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"
        return board


        