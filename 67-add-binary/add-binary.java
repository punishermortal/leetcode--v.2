class Solution {
    public String addBinary(String binary1, String binary2) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int i = binary1.length() - 1;
        int j = binary2.length() - 1;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) sum += binary1.charAt(i--) - '0';
            if (j >= 0) sum += binary2.charAt(j--) - '0';
            result.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) result.append(carry);
        return result.reverse().toString();
    }
}