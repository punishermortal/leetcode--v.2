class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int xor = 0;
        for(int i=0; i<nums.length; i++){
            xor ^= nums[i];
        }

        int[] res = new int[nums.length];
        int maxor = (int)Math.pow(2, maximumBit)-1;
        for(int i=0; i<nums.length; i++){
            res[i] = xor^maxor;
            xor ^= nums[nums.length-i-1];
        }
        return res;
    }
}