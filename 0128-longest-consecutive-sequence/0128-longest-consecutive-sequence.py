class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=1
        current=1
        nums=sorted(set(nums))
        if nums==[]:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-(nums[i-1])==1:
                current+=1
            else:
                longest=max(current,longest)
                current=1
        return max(longest,current)
        