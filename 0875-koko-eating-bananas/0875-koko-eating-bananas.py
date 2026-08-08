import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while(low<=high):
            reqTime=0
            mid=(low+high)//2
            for banana in piles:
                reqTime+=math.ceil(banana/mid)
            if reqTime<=h:
                high=mid-1
            else:
                low=mid+1
        return low
      

    
        
            

        