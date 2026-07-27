from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        q=deque()
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            value=q.popleft()
            topo.append(value)
            for nei in adj[value]:
                if indegree[nei]!=0:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            
        if len(topo)==numCourses:
            return True
        else:
            return False
            





        