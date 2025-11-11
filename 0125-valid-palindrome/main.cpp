#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string dummy;
        for (char c : s) {
            if (isalnum(c)) {              
                dummy += tolower(c);       
            }
        }

        int left = 0, right = dummy.size() - 1;
        while (left < right) {             
            if (dummy[left] != dummy[right]) return false;
            left++;
            right--;
        }

        return true;
    }
};
