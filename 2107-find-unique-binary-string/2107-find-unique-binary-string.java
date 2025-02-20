class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        // Convert the binary strings to their decimal representation
        int[] decimalValues = new int[n];
        for (int i = 0; i < n; i++) {
            int decimal = 0;
            for (int j = 0; j < n; j++) {
                decimal = (decimal << 1) | (nums[i].charAt(j) == '1' ? 1 : 0);
            }
            decimalValues[i] = decimal;
        }

        // Increment until we find a number not in the array
        int counter = 0;
        while (isPresentInArray(counter, decimalValues)) {
            counter++;
        }

        // Convert the result back to a binary string of length n
        return convertToBinaryString(counter, n);
    }

    // Check if the given decimal number exists in the array
    private boolean isPresentInArray(int num, int[] decimalValues) {
        for (int value : decimalValues) {
            if (value == num) {
                return true;
            }
        }
        return false;
    }

    // Convert a number to a binary string of a given length
    private String convertToBinaryString(int num, int length) {
        StringBuilder binaryString = new StringBuilder();
        for (int i = length - 1; i >= 0; i--) {
            binaryString.append((num >> i) & 1);
        }
        return binaryString.toString();
    }
}
