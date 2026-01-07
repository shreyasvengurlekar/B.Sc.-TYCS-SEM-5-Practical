graph = {
    'Kankavli': [('Malvan', 10), ('Kudal', 5)],
    'Kudal': [('Vengurla', 8), ('Sawantwadi', 4), ('Malvan', 6)],
    'Vengurla': [('Sawantwadi', 3), ('Kudal', 8)],
    'Sawantwadi': [('Kudal', 4), ('Vengurla', 3)],
    'Malvan': [('Kudal', 6), ('Kankavli', 10)]
}

visited=set()
def dfs(visited,graph,node):
    sum1=0
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour,weight in graph[node]:
            dfs(visited,graph,neighbour)
            if(node==destination):
                break
print("Following is the depth first search")
source=input("Enter the starting point")
destination=input("Enter the destination")
dfs(visited,graph,source)


