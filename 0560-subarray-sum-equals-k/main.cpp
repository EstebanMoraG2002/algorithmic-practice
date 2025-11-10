#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixCount;
        
        prefixCount[0] = 1;

        int prefixSum = 0;
        int result = 0;

        for(int num: nums){
            prefixSum += num;
            int need = prefixSum-k;
            if(prefixCount.find(need)!= prefixCount.end()){
                result += prefixCount[need];
            }
            prefixCount[prefixSum]++;
        }

        return result;
    }
};