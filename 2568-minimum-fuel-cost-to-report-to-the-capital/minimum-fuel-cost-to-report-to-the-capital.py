class Solution:
    def minimumFuelCost(self, roads, seats):
        from collections import defaultdict
        
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        fuel = 0
        
        def dfs(node, parent):
            nonlocal fuel
            people = 1
            
            for nei in graph[node]:
                if nei != parent:
                    people += dfs(nei, node)
            
            if node != 0:
                fuel += (people + seats - 1) // seats
            
            return people
        
        dfs(0, -1)
        return fuel
