# Count of connected components in an undirected graph
# import numpy as np

def count_components(A):
    n = len(A)
    visited = [False] * n
    components = 0

    def dfs(v):
        visited[v] = True
        for u in range(n):
            if A[v][u] and not visited[u]:
                dfs(u)

    for v in range(n):
        if not visited[v]:
            dfs(v)
            components += 1

    return components

A = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

print(count_components(A))