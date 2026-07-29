class Solution(object):
    def maxArea(self, height):
        leftmax=0
        rightmax=len(height)-1
        ans=0
        while(leftmax<rightmax):
            breadth=rightmax-leftmax
            area=min(height[rightmax],height[leftmax])*breadth
            ans=max(ans,area)
            if height[leftmax]<height[rightmax]:
                leftmax+=1
            else:
                rightmax-=1
        return ans



            

        
        