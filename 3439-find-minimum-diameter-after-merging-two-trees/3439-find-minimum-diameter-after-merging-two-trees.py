class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(adj):
            def bfs(node):
                q = deque()
                q.append((node,0))
                vis = set([node])
                max_dis= 0
                max_node = node
                while q:
                    i,d = q.popleft()
                    if d>max_dis:
                        max_dis = d
                        max_node = i
                    for v in adj[i]:
                        if v not in vis:
                            vis.add(v)
                            q.append((v,d+1))
                return (max_node,max_dis)
            fnode , _  = bfs(0)
            _ , diameter = bfs(fnode)
            return diameter
        adj1 = defaultdict(list)
        adj2 =  defaultdict(list)
        for x,y in edges1:
            adj1[x].append(y)
            adj1[y].append(x)
        for x,y in edges2:
            adj2[x].append(y)
            adj2[y].append(x)
        d1  = diameter(adj1)
        d2  = diameter(adj2)
        print(d1,d2)
        return max(d1,d2,(d1+1)//2 + 1  + (d2+1)//2)