class Solution {
    public int maxSubArray(int[] nums) {
        int currsum=0;
        int maxi=nums[0];
        for (int num:nums){
            if (currsum<0){
                currsum=0;
            }
            currsum+=num;
            maxi=Math.max(currsum,maxi);
        }
        return maxi;
    }
}