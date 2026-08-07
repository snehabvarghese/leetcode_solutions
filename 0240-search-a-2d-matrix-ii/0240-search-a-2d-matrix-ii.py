class Solution(object):
    def searchMatrix(self, nums, target):
        row=0
        col=len(nums[0])-1
        while(row<len(nums) and col >=0):
            if nums[row][col]==target:
                return True
            elif nums[row][col]<target:
                row+=1
            else:
                col-=1
        return False