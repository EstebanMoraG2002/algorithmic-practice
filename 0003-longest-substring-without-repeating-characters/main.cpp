#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastSeen;
        int maxLen = 0;
        int start = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (lastSeen.find(s[i]) != lastSeen.end() && lastSeen[s[i]] >= start) {
                start = lastSeen[s[i]] + 1;
            }
            lastSeen[s[i]] = i;
            maxLen = max(maxLen, i - start + 1);
        }

        return maxLen;
    }
};

// Example usage for testing (LeetCode runs main internally)
#include <iostream>
int main() {
    Solution sol;
    cout << sol.lengthOfLongestSubstring("abcabcbb") << endl; // 3
    cout << sol.lengthOfLongestSubstring("bbbbb") << endl;    // 1
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl;   // 3
    cout << sol.lengthOfLongestSubstring("abba") << endl;     // 2
}
