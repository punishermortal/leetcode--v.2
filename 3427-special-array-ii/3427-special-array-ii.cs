public class Solution {
    public bool[] IsArraySpecial(int[] nums, int[][] queries) {

        int n = nums.Length;
        // Array to store the alternating parity information for each element
        int[] same = new int[n];
        // Variable to store the parity of the first element odd or even
        int prev = nums[0] % 2;

        // Preprocess (nums) array to build (same) array that tracks the count of continuous special subarrays
        for (int i = 1; i < n; i++) 
        {
            // Copy the value from the previous index to carry over the same count
            same[i] = same[i - 1];
            int curr = nums[i] % 2;

            // Check if the current element has the same parity as the previous element
            // If it have the same parity, the subarray is no longer special
            if (curr == prev) 
            {
                same[i]++;
            }
            prev = curr;
        }

        // Array to store the boolean results for each query
        int qLength = queries.Length;
        bool[] result = new bool[qLength];

        // Process each query to check if the subarray is special
        for (int q = 0; q < qLength; q++) 
        {
            // Compare same[to i] and same[from i] to check if the subarray from (from i) to (to i) is special
            // If it's equal, it means the subarray is special or has alternating parity, otherwise it's not
            int[] query = queries[q];
            result[q] = same[query[1]] == same[query[0]];
        }
        // Return the results for all queries
        return result;
    }
}