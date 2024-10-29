class Solution {
    public int findTheLongestSubstring(String s) {
        Map<Integer, Integer> map = new HashMap<>(Map.of(0, -1));
        Map<Character, Integer> dict = Map.of('a', 0, 'e', 1, 'i', 2, 'o', 3, 'u', 4);
        int curr = 0, max = 0;
        for (int i = 0; i < s.length(); i++) {
            curr ^= dict.get(s.charAt(i)) != null ? (1 << dict.get(s.charAt(i))) : 0;
            max = Math.max(max, i - map.getOrDefault(curr, Integer.MAX_VALUE));
            map.put(curr, Math.min(map.getOrDefault(curr, Integer.MAX_VALUE), i));      
        }
        return max;
    }
}