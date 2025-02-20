class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Mapping positions to their colors and keeping track of color counts
        position_map, color_map, result, unique_colors = {}, {}, [], 0
        
        for position, new_color in queries:
            # If the position already has a ball, decrement the color count
            if position in position_map:
                old_color = position_map[position]
                color_map[old_color] -= 1
                if color_map[old_color] == 0:
                    unique_colors -= 1
            
            # Assign the new color to the position and update the color count
            position_map[position] = new_color
            color_map[new_color] = color_map.get(new_color, 0) + 1
            
            # If it's a new color being added, increase the unique color count
            if color_map[new_color] == 1:
                unique_colors += 1
            
            # Append the current number of unique colors to the result list
            result.append(unique_colors)
        
        return result
