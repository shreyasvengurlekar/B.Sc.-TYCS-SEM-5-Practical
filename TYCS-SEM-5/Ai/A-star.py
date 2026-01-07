# Directed graph with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic (estimated cost from node to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'

# A* Algorithm
open_list = [start]
came_from = {}
g_score = {start: 0}
f_score = {start: heuristic[start]}

while open_list:
    # Pick node with smallest f_score
    current = min(open_list, key=lambda x: f_score.get(x, float('inf')))
    print("Current node:", current)

    if current == goal:
        print("Goal reached!")
        break

    open_list.remove(current)

    for neighbor, cost in graph[current]:
        tentative_g = g_score[current] + cost
        if tentative_g < g_score.get(neighbor, float('inf')):
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            f_score[neighbor] = tentative_g + heuristic[neighbor]
            if neighbor not in open_list:
                open_list.append(neighbor)

# Reconstruct path
path = [goal]
while path[-1] in came_from:
    path.append(came_from[path[-1]])
path.reverse()

print("Shortest path:", path)
print("Cost:", g_score[goal])
