/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public int minimumOperations(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        int cnt = 0;
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<Integer> list = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.remove();
                list.add(node.val);
                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
            }
            cnt += minSwaps(list);
        }
        return cnt;
    }

    private static int minSwaps(ArrayList<Integer> nums) {
        int n = nums.size();

        // Step 1: Create a list of pairs
        List<Pairs> pairs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            pairs.add(new Pairs(nums.get(i), i));
        }

        // Step 2: Sort the list based on array values
        pairs.sort(Comparator.comparingInt(p -> p.value));

        // Step 3: Create a visited list
        boolean[] visited = new boolean[n];
        Arrays.fill(visited, false);

        // Step 4: Calculate swaps by finding cycles
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            // If already visited or in the correct position, skip
            if (visited[i] || pairs.get(i).index == i) {
                continue;
            }

            // Trace the cycle
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = pairs.get(j).index; // Move to the next index in the cycle
                cycleSize++;
            }

            // Add the swaps required for this cycle
            if (cycleSize > 1) {
                swaps += (cycleSize - 1);
            }
        }

        return swaps;
    }

    // Static nested class for Pairs
    private static class Pairs {
        int value, index;

        Pairs(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}