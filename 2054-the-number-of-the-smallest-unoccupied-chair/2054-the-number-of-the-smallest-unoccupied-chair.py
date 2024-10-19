import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        n = len(times)
        
        for friend_id, (arrival, leaving) in enumerate(times):
            events.append((arrival, friend_id, 'arrive'))
            events.append((leaving, friend_id, 'leave'))
        events.sort(key=lambda x: (x[0], x[2] == 'arrive'))
        available_chairs = []
        occupied_chairs = {}
        current_chair = 0
        for time, friend_id, event_type in events:
            if event_type == 'arrive':
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = current_chair
                    current_chair += 1
                occupied_chairs[friend_id] = chair
                if friend_id == targetFriend:
                    return chair
            else:
                chair = occupied_chairs[friend_id]
                heapq.heappush(available_chairs, chair)