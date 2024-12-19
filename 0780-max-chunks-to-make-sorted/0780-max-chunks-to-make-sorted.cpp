class Solution {
public:

    //Time Complexity-> O(n)
    //Space Complexity-> O(1)
    int maxChunksToSorted(vector<int>& arr) {
        int n=arr.size();
        int sum=0,cnt=0;
        //sum will store the sum till the current index
        //cnt will store number of chunks

        //If arr was sorted, then number at ith index will be -> i
        //So the sum till ith index will be i*(i+1)/2

        //so at any point if the sum==i*(i+1)/2 it can form a chunk
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if((sum==(i*(i+1))/2))cnt++;
        }

        return cnt;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();