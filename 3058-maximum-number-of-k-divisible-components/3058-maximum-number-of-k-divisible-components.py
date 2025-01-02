from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # Initialize variables
        self.components = 0

        def dfs(node: int, parent: int) -> int:
            # Calculate the sum of the subtree rooted at `node`
            subtree_sum = values[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)

            # If the subtree sum is divisible by k, it's a valid component
            if subtree_sum % k == 0:
                self.components += 1
                return 0  # Reset the sum to split the component

            return subtree_sum

        # Start DFS from the root node (0 assumed as the root)
        dfs(0, -1)

        return self.components