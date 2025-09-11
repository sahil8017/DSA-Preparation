class Solution {
public:
    int strStr(string haystack, string needle) {
        auto pos = haystack.find(needle);
        if (pos == string::npos) {  // Use string::npos instead of -1
            return -1;
        }
        return (int)pos;
    }
};
