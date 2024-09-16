# -*- coding: utf-8 -*-

def shortest_path(n,w):
    # d = [[0 for _ in range(n)] for _ in range(n)]
    d = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # # mid = [[None for _ in range(n)] for _ in range(n)]
    mid = [[None, None, None, None],[None, None, None, None],[None, None, None, None],[None, None, None, None]]
    
    # d = [[],[],[],[]]
    
    for i in range(n):
        for j in range(n):
            d[i][j] = w[i][j]
            mid[i][j] = None
    for k in range(n): # Consider each node k as an intermediate node
        temp = []
        for i in range(n):    # Consider all pairs of nodes (i, j)
            for j in range(n):
                # If the path through k is shorter, update it
                                
                temp.append(d[i][j])
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    mid[i][j] = k  
        print("temp ----------->", temp)
    return d , mid
n=4                


w = [
    [0, 8, float('inf'), 1],
    [float('inf'), 0, 1, float('inf')],
    [4, float('inf'), 0, float('inf')],
    [float('inf'), 2, 9, 0]
]

shortest_distances, intermediates = shortest_path(n,w)
# Print the shortest distance matrix
print("Shortest Distances:")
for row in shortest_distances:
    print(row)

# Print the intermediate nodes
print("\nIntermediate Nodes:")
for row in intermediates:
    print(row)