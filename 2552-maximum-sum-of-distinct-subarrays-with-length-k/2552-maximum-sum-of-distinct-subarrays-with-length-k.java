class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        
        HashMap<Integer,Integer> hm = new HashMap<>();
        int l=0,r=0,n=nums.length;
        
        long ans =0,sum=0;;

        for(int i=0;i<k;i++)
        {
            hm.put(nums[i],hm.getOrDefault(nums[i],0)+1);
            sum +=nums[i];
        }
        if(hm.size()==k) ans = sum;
        r=k;
        while(r<n)
        {
            if(hm.size()==k) ans = Math.max(ans,sum);
            sum -= nums[l];
            hm.put(nums[l],hm.get(nums[l])-1);
            if(hm.get(nums[l])==0) hm.remove(nums[l]);
            l++;
            sum +=nums[r];
            hm.put(nums[r],hm.getOrDefault(nums[r],0)+1);
            if(hm.size()==k) ans = Math.max(ans,sum);
            r++;
        }
        return ans;
    }
}