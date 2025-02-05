class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int a[] = new int[26];

        for(char c: s1.toCharArray())
        {
            a[c - 'a']++;
        }

        int b[] = new int[26];

        for(char c: s2.toCharArray())
        {
            b[c - 'a']++;
        }

        for(int i = 0; i < 26; i++)
        {
            if(a[i] != b[i])
            {
                return false;
            }
        }

        int count = 0;

        for(int i = 0; i < s1.length(); i++)
        {
            if(s1.charAt(i) != s2.charAt(i))
            {
                count++;
            }
        }

        return count <= 2;
    }
}