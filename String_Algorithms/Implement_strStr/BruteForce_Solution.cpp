
class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length(), m = needle.length();

        // If needle is an empty string, return 0
        if (m == 0)
            return 0;

        // Loop through haystack to check for matching substring
        for (int i = 0; i <= n - m; i++) { // Include n-m position
            bool found = true;
            for (int j = 0; j < m; j++) {
                if (haystack[i + j] != needle[j]) {
                    found = false;
                    break;
                }
            }

            if (found) {
                return i; // Return the index of the first occurrence
            }
        }

        return -1; // Return -1 if no match is found
    }
};
