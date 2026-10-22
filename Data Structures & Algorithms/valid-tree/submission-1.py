class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        stack = set()
        vertices = {}
        visited = set()
        has_cycle = False

        for v in edges:
            if v[0] not in vertices:
                vertices[v[0]] = {v[1]}
                if v[1] not in vertices:
                    vertices[v[1]] = {v[0]}
                else:
                    vertices[v[1]].add(v[0])        
            else:
                vertices[v[0]].add(v[1])
                if v[1] not in vertices:
                    vertices[v[1]] = {v[0]}
                else:
                    vertices[v[1]].add(v[0])      

        def dfs(curr_v,parent):
            nonlocal has_cycle
            visited.add(curr_v)
            if curr_v not in vertices:
                return
            stack.add(curr_v)
            for v in vertices[curr_v]:
                if v not in visited:
                    dfs(v,curr_v)
                else:
                    if v in stack and v != parent :
                        has_cycle = True    
            stack.remove(curr_v)        

        dfs(0, None)
        return n == len(visited) and has_cycle == False