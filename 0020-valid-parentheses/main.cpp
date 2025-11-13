#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        string open = "([{";
        string close = ")]}";
        stack<char> st;

        for (char c : s) {
            size_t posOpen = open.find(c);
            if (posOpen != string::npos) {
                st.push(c);
                continue;
            }

            size_t posClose = close.find(c);
            if (posClose != string::npos) {
                if (st.empty()) return false;               
                if (st.top() != open[posClose]) return false; 
                st.pop();
                continue;
            }

            return false;
        }

        return st.empty();
    }
};
