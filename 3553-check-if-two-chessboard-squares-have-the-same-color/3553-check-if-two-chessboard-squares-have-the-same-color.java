class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int val1 = coordinate1.charAt(0) - 97 + 1;
        int val2 = coordinate2.charAt(0) - 97 + 1;
        int val3 = coordinate1.charAt(1) - '0';
        int val4 = coordinate2.charAt(1) - '0';
        if((val1 + val3) % 2 == (val2 + val4) % 2) return true;
        return false;
    }
}