

import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], start)]  # (priority, node)
    
    while pq:
        _, current = heapq.heappop(pq)
        print(current, end=" ")

        if current == goal:
            print("\nGoal found!")
            return

        visited.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

# Example graph (directed)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (lower means closer to goal)
heuristic = {
    'A': 5, 'B': 4, 'C': 2, 'D': 7, 'E': 3, 'F': 0
}

best_first_search(graph, 'A', 'F', heuristic)
