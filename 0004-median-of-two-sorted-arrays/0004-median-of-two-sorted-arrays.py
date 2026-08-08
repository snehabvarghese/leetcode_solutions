class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        left=0
        right=0
        while(left<len(nums1) and right<len(nums2)):
            if nums1[left]>nums2[right]:
                merged.append(nums2[right])
                right+=1
            else:
                merged.append(nums1[left])
                left+=1
        while(right<len(nums2)):
            merged.append(nums2[right])
            right+=1
        while(left<len(nums1)):
            merged.append(nums1[left])
            left+=1
        
        middle=(len(merged))//2
        if len(merged)%2==0:
            
            median=(merged[middle]+merged[middle-1])/2
        elif len(merged)%2!=0:
            median=merged[middle]
        return median       