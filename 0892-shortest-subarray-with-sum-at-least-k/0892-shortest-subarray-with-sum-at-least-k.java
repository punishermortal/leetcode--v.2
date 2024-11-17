class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n=nums.length;
        if(n==1)
        {
            if(nums[0]>=k)
            {
                return 1;
            }
            else
            {
                return -1;
            }
        }
        long[] prefixSum=new long[n+1];
        for(int i=0;i<n;i++)
        {
            prefixSum[i+1]=prefixSum[i]+nums[i];
        }
        int minLength=Integer.MAX_VALUE;
        int[] q=new int[n+1];
        int l=0,r=0;
        for(int i=0;i<=n;i++)
        {
            while(r>l && prefixSum[i]-prefixSum[q[l]]>=k)
            {
                minLength=Math.min(minLength,i-q[l++]);
            }
            while(r>l && prefixSum[i]<=prefixSum[q[r-1]])
            {
                r--;
            }
            q[r++]=i;
        }
        return minLength>n?-1:minLength;
    }
}