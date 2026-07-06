class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        res=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True):
            if len(res)==k:
                break
            
            res.append(key)
        
            
        return res

        