from collections import defaultdict, deque
from typing import List, Set, Dict, Optional
import heapq

class Graph:
    def __init__(self, directed: bool = False):
        self.graph = defaultdict(list)
        self.directed = directed
        
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add edge between vertices u and v"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def bfs(self, start: int) -> List[int]:
        """Breadth-First Search
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        result = []
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result

    def dfs(self, start: int) -> List[int]:
        """Depth-First Search
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        result = []
        
        def dfs_util(vertex: int):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result

    def detect_cycle(self) -> bool:
        """Detect cycle in the graph using DFS
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        rec_stack = set()
        
        def has_cycle(vertex: int) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if has_cycle(vertex):
                    return True
        return False

    def topological_sort(self) -> List[int]:
        """Topological Sort (for DAG)
        Time: O(V + E), Space: O(V)
        """
        if not self.directed or self.detect_cycle():
            raise ValueError("Graph must be a DAG")
            
        visited = set()
        stack = []
        
        def dfs_util(vertex: int):
            visited.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)
            
            stack.append(vertex)
        
        for vertex in self.graph:
            if vertex not in visited:
                dfs_util(vertex)
        
        return stack[::-1]

    def dijkstra(self, start: int) -> Dict[int, int]:
        """Dijkstra's Shortest Path Algorithm
        Time: O((V + E)logV), Space: O(V)
        """
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

    def bellman_ford(self, start: int) -> Dict[int, int]:
        """Bellman-Ford Algorithm (handles negative weights)
        Time: O(VE), Space: O(V)
        """
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        
        # Relax all edges V-1 times
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        # Check for negative weight cycles
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")
        
        return distances

    def prim_mst(self) -> List[tuple]:
        """Prim's Minimum Spanning Tree Algorithm
        Time: O((V + E)logV), Space: O(V)
        """
        if self.directed:
            raise ValueError("Prim's algorithm works only for undirected graphs")
            
        mst = []
        visited = {next(iter(self.graph))}
        edges = [
            (weight, u, v) 
            for u in self.graph 
            for v, weight in self.graph[u]
        ]
        heapq.heapify(edges)
        
        while edges and len(visited) < len(self.graph):
            weight, u, v = heapq.heappop(edges)
            if u in visited and v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
            elif v in visited and u not in visited:
                visited.add(u)
                mst.append((v, u, weight))
                
        return mst

    def find_bridges(self) -> List[tuple]:
        """Find all bridges in the graph
        Time: O(V + E), Space: O(V)
        """
        discovery = {}
        low = {}
        time = [0]
        bridges = []
        
        def dfs(vertex: int, parent: Optional[int]):
            discovery[vertex] = low[vertex] = time[0]
            time[0] += 1
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in discovery:
                    dfs(neighbor, vertex)
                    low[vertex] = min(low[vertex], low[neighbor])
                    
                    if low[neighbor] > discovery[vertex]:
                        bridges.append((vertex, neighbor))
                elif neighbor != parent:
                    low[vertex] = min(low[vertex], discovery[neighbor])
        
        for vertex in self.graph:
            if vertex not in discovery:
                dfs(vertex, None)
                
        return bridges
