class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow=0, fast =0;
        for(int n: nums){
            if(fast+1<nums.size() && nums[slow]!=nums[fast+1]){
                nums[++slow] = nums[fast+1];
            }
            fast++;
        }
        return slow+1;
    }
};