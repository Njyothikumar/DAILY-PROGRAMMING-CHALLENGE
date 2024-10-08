from collections import deque, defaultdict

def shortest_path(V, edges, start, end):
    # Step 1: Construct the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    
    #  Initialize BFS
    queue = deque([(start, 0)])  
    visited = set()
    visited.add(start)
    
    while queue:
        current, depth = queue.popleft()
        
        # Check if we have reached the end node
        if current == end:
            return depth
        
        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    
    return -1

# Example usage
V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4
print(shortest_path(V, edges, start, end))  
V2 = 3
edges2 = [[0, 1], [1, 2]]
start2 = 0
end2 = 2
print(shortest_path(V2, edges2, start2, end2))  

V3 = 4
edges3 = [[0, 1], [1, 2]]
start3 = 2
end3 = 3
print(shortest_path(V3, edges3, start3, end3)) 
