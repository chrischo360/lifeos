from graph import Graph

def test_graph_algorithms():
    # Create a directed graph for testing
    g = Graph(directed=True)
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("BFS starting from vertex 2:", g.bfs(2))
    print("DFS starting from vertex 2:", g.dfs(2))
    print("Has cycle:", g.detect_cycle())
    
    # Create a DAG for topological sort
    dag = Graph(directed=True)
    dag.add_edge(5, 2)
    dag.add_edge(5, 0)
    dag.add_edge(4, 0)
    dag.add_edge(4, 1)
    dag.add_edge(2, 3)
    dag.add_edge(3, 1)
    
    print("Topological Sort:", dag.topological_sort())
    
    # Create a weighted graph for shortest path algorithms
    weighted_graph = Graph(directed=True)
    weighted_graph.add_edge(0, 1, 4)
    weighted_graph.add_edge(0, 2, 2)
    weighted_graph.add_edge(1, 2, 3)
    weighted_graph.add_edge(2, 3, 2)
    weighted_graph.add_edge(3, 1, -1)
    
    print("Dijkstra's shortest paths from vertex 0:", weighted_graph.dijkstra(0))
    print("Bellman-Ford shortest paths from vertex 0:", weighted_graph.bellman_ford(0))
    
    # Create an undirected graph for MST and bridges
    undirected_graph = Graph()
    undirected_graph.add_edge(0, 1, 4)
    undirected_graph.add_edge(0, 2, 2)
    undirected_graph.add_edge(1, 2, 1)
    undirected_graph.add_edge(2, 3, 3)
    
    print("Minimum Spanning Tree:", undirected_graph.prim_mst())
    print("Bridges:", undirected_graph.find_bridges())

if __name__ == "__main__":
    test_graph_algorithms()
