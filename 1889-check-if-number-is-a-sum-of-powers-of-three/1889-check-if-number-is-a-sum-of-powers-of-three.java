class Solution {
    public boolean checkPowersOfThree(int n) {
        while(n>0){
            int rem = n%3;
            if (rem == 2){
                return false;
            }
            n=(int)(n/3);
        }
        return true;
    }
}