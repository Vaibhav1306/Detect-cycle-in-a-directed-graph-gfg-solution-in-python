def isCyclic(self,V,adj):
        visited = [0]*V
        helper = [0]*V
        for i in range(V):
            if visited[i] == 0:
                ans = self.DFS(i,visited,helper,adj)
                if ans == 1:
                    return 1
        return 0


    def DFS(self,i, visited,helper,adj):
        visited[i] = 1
        helper[i] = 1
        neighbours = adj[i]
        for k in range(len(neighbours)):
            curr = neighbours[k]
            if helper[curr] == 1:
                return 1
            if visited[curr] == 0:
                ans = self.DFS(curr,visited,helper,adj)
                if ans == 1:
                    return 1
        helper[i] = 0
        return 0
        
