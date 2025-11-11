#include <vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slow =0, fast =0;

        for(int n: nums){
            if(nums[fast]!=val){
                nums[slow++] = nums[fast];
            }
            fast++;
        }
        return slow;
    }
};