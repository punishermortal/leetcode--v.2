from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, grid: List[List[int]]) -> int:
        goal = "123450"
        initial_state = ''.join(str(num) for row in grid for num in row)
        
        move_map = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        states_queue = deque([(initial_state, 0)])
        seen_states = set()
        seen_states.add(initial_state)
        
        while states_queue:
            current_state, step_count = states_queue.popleft()
            if current_state == goal:
                return step_count
            zero_pos = current_state.index('0')
            for swap_pos in move_map[zero_pos]:
                new_grid = list(current_state)
                new_grid[zero_pos], new_grid[swap_pos] = new_grid[swap_pos], new_grid[zero_pos]
                new_state = ''.join(new_grid)
                if new_state not in seen_states:
                    seen_states.add(new_state)
                    states_queue.append((new_state, step_count + 1))
        
        return -1
