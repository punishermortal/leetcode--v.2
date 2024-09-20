class Solution {
public:
     int LPS(string& s) {           
        int n = s.length();
        vector<int> lps(n);
        for (int i = 1; i < n; i++) {
            int len = lps[i - 1];
            if (s[i] == s[len]) {
                lps[i] = len + 1;
            } else {
                while (s[i] != s[len]) {
                    if (len == 0) {
                        len = -1;
                        break;
                    }
                    len = lps[len - 1];
                }
                lps[i] = len + 1;
            }
        }
        return lps[n - 1];
    }

    string shortestPalindrome(string s) {
        string rev = s;
        reverse(rev.begin() , rev.end());

        string str = s + "#" + rev;
        int lps = LPS(str);

        string toAdd = s.substr(lps);
        reverse(toAdd.begin(),toAdd.end());

        return toAdd + s;
    }
};