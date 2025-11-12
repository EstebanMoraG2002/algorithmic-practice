class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        if(nums.empty()) return 0;

        int left=0;
        double average = -1e9, sum=0.0;
        for(int right=0; right<nums.size(); ++right){
            sum+=nums[right];
            if(right-left+1 == k){
                average = max(average, sum/k);
                sum-=nums[left];
                left++;
            }
        }
        return average;
    }
};