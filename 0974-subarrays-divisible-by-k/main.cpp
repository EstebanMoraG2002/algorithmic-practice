#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> prefixCount;
        prefixCount[0]=1;

        int prefixSum = 0;
        int result = 0;

        for(int num: nums){
            prefixSum += num;
            int remainder = prefixSum % k;

            if(remainder<0) remainder+=k;

            if(prefixCount.find(remainder)!=prefixCount.end()){
                result += prefixCount[remainder];
            }

            prefixCount[remainder]++;
        }

        return result;

    }
};