class Solution {
    public int findKthNumber(int n, int k) {
        int current = 1;
        int counter = 1;
        while (counter < k) {
            int stepCount = calculateSteps(current, n);
            if (counter + stepCount <= k) {
                current += 1;
                counter += stepCount;
            } else {
                current *= 10;
                counter++;
            }
        }
        return current;
    }
    private int calculateSteps(long current, int limit) {
        int totalSteps = 0;
        long next = current + 1;
        while (current <= limit) {
            totalSteps += Math.min(next, limit + 1) - current;
            current *= 10;
            next *= 10;
        }
        return totalSteps;
    }
}