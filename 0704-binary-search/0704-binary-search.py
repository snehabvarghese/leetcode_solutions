class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                right=mid-1
            if target>nums[mid]:
                left=mid+1
        return -1
                    