from collections import deque
class Solution(object):
    def check(self,nei,node,color,graph,q):
        for i in range(len(color)):
            
            
            if color[nei]==-1:
                color[nei]=1-color[node]
                q.append(nei)
            if color[nei]==color[node]:
                return False
        return True
        
        

    def isBipartite(self, graph):
        color =[-1 for _ in range(len(graph))]
       
        q=deque()
        for i in range(len(graph)):
                if color[i]==-1:
                    color[i]=0
                    q.append(i)
                    while q:
            
                        node=q.popleft()
            
                        for nei in graph[node]:
                
                            if (self.check(nei,node,color,graph,q)==False):
                    
                                return False
                
                
        return True
        
        
        