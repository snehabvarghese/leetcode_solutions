class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        count=0
        end=float("-inf")
        for start,finish in pairs:
            if start>end:
                count+=1
                end=finish


            
        return count

            
            
        