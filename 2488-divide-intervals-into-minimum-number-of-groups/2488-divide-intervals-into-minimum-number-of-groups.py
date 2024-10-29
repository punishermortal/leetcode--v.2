class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times_sorted = sorted(interval[0] for interval in intervals)
        end_times_sorted = sorted(interval[1] for interval in intervals)
        
        end_index, group_counter = 0, 0

        # Traverse through sorted start times to calculate required groups
        for current_start in start_times_sorted:
            if current_start > end_times_sorted[end_index]:
                end_index += 1
            else:
                group_counter += 1

        return group_counter