#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> myMap;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (myMap.find(complement) != myMap.end()) {
                return {myMap[complement], i};
            }
            myMap[nums[i]] = i;
        }

        return {}; 
    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> res1 = sol.twoSum(nums1, target1);
    cout << "[" << res1[0] << "," << res1[1] << "]" << endl;

    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> res2 = sol.twoSum(nums2, target2);
    cout << "[" << res2[0] << "," << res2[1] << "]" << endl;

    vector<int> nums3 = {3, 3};
    int target3 = 6;
    vector<int> res3 = sol.twoSum(nums3, target3);
    cout << "[" << res3[0] << "," << res3[1] << "]" << endl;

    return 0;
}
