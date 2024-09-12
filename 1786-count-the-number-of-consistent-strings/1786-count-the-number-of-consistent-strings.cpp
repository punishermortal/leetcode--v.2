class Solution {
private:
    bool helper(string word, unordered_set<char> &us){
        bool ans = true;
        for(auto &ch : word){
            ans = ans && (us.find(ch) != us.end());
        }
        return ans;
    }
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        int ans = 0;
        unordered_set<char> us;
        for(auto &ch : allowed) us.insert(ch);
        for(auto &word : words) {
            ans += helper(word, us);
        }
        return ans;
    }
};