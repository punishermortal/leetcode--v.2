class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        list_of_pairs = []
        res = 1
        pairs.sort(key=lambda pair: pair[1])
        end_meeting_time =  pairs[0][1]
        
        for i in range(1,len(pairs)):
            start_time =pairs[i][0]
            if start_time > end_meeting_time:
                res+=1
                end_meeting_time  = pairs[i][1]
        return res