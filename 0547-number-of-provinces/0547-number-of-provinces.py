class Solution(object):
    def dfs(self,i,adjL,visited):
        visited[i]=1
        for nei in adjL[i]:
            if visited[nei]==0:
                self.dfs(nei,adjL,visited)
        
    def findCircleNum(self, isConnected):
        r=len(isConnected)
        c=len(isConnected[0])
        adjL=[[] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i!=j and isConnected[i][j]==1:
                    adjL[i].append(j)
                    adjL[j].append(i)
        visited=[0]*r
        count=0
        for i in range(r):
            if visited[i]==0:
                count+=1
                self.dfs(i,adjL,visited)
        return count




        