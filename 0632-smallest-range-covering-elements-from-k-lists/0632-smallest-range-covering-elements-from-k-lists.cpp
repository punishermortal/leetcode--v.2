class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        
        int n = nums.size();
        vector<pair<int,int>> vec;
        
        // Step 1: Flatten the input into a single vector of pairs
        for(int i = 0; i < n; i++) {
            for(auto& k: nums[i]) {
                vec.push_back({k, i});
            }
        }
        
        // Step 2: Sort the flattened vector
        sort(vec.begin(), vec.end());
        
        unordered_map<int,int> mp;
        int j = 0;
        vector<pair<int,int>> check;
        
        // Step 3: Use sliding window to find valid ranges
        for(int i = 0; i < vec.size(); i++) {
            while(j < vec.size() && mp.size() < n) {
                mp[vec[j].second]++;
                j++;
            }
            
            if(mp.size() == n) {
                check.push_back({vec[i].first, vec[j-1].first});
            }
            
            mp[vec[i].second]--;
            if(mp[vec[i].second] == 0) mp.erase(vec[i].second);
        }
        
        // Step 4: Find the smallest range from valid ranges
        int mini = INT_MAX;
        vector<int> ans(2);
        for(int i = 0; i < check.size(); i++) {
            if(mini > check[i].second - check[i].first) {
                mini = check[i].second - check[i].first;
                ans[0] = check[i].first;
                ans[1] = check[i].second;
            }
            else if(mini == check[i].second - check[i].first) {
                if(ans[0] > check[i].first) {
                    ans[0] = check[i].first;
                    ans[1] = check[i].second;
                }
            }
        }
        
        return ans;
    }
};