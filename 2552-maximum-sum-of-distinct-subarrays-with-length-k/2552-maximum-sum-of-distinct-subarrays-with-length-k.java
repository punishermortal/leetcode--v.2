class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int i=0;
        int j=0;
        long sum=0;
        long maxi=0;
        HashMap<Integer,Integer>hm=new HashMap<>();
        while(j<nums.length){
            sum+=nums[j];
            hm.put(nums[j],hm.getOrDefault(nums[j],0)+1);
            if(j-i+1<k){
                j++;
            }
            else if(j-i+1==k){
                if(hm.size()==k){
                    System.out.println(hm.size());
                    maxi=Math.max(maxi,sum);
                }
                i++;
                j++;
                sum=sum-(long)nums[i-1];
                if(hm.get(nums[i-1])==1){
                    hm.remove(nums[i-1]);
                }else{
                    hm.put(nums[i-1],hm.get(nums[i-1])-1);
                }
                
            }
        }
        return maxi;
    }
}