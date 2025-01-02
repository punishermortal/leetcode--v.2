class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int i=0, j=0; //Two Pointers

        while(i<str1.length() && j<str2.length()){
            if(str1.charAt(i)-'a'==str2.charAt(j)-'a' || (str1.charAt(i)-'a'+1)%26==str2.charAt(j)-'a'){
                j++;
            }
            if(j==str2.length()){
                return true;
            }
            i++;
        }

        return false;
    }
}