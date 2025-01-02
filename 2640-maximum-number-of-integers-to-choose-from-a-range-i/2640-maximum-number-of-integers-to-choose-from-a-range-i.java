class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        Set<Integer> bannedSet = new HashSet<>();
        for (int num : banned) {
            bannedSet.add(num);
        }
        int currentSum = 0, count = 0;
        for (int i = 1; i <= n; i++) {
            if (!bannedSet.contains(i)) {
                if (currentSum + i <= maxSum) {
                    currentSum += i;
                    count++;
                } else {
                    break;
                }
            }
        }
        return count;
    }
}