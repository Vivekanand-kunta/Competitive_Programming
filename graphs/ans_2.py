class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.array=[[] for i in range(vertices)]
    def add(self,vertex,destination):
        self.array[vertex].append(destination)
    def detect_cycle(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for node in range(self.vertices):
            if self.detect_cycle_rec(node,visited,rec_stack):
                return True
        return False
    def detect_cycle_rec(self, node, visited, rec_stack):
        
        if rec_stack[node]:
            return True
        if visited[node]:
            return False
        
        visited[node]=True
        rec_stack[node]=True

        for neighbor in self.array[node]:
            if not visited[neighbor]:
                if self.detect_cycle_rec(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[node] = False
        return False


class Solution:
    def canFinish(self, cou: int, req: List[List[int]]) -> bool:
        g=graph(cou)
        for ele in req:
            g.add(ele[0],ele[1])
        return not g.detect_cycle()
        
        
