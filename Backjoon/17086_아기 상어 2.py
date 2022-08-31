from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))


def bfs():

    while q:
        r, c = q.popleft()
        dr = [1, -1, 0, 0, 1, 1, -1, -1]
        dc = [0, 0, 1, -1, 1, -1, 1, -1]

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))

bfs()
dist = 0
for i in range(n):
    for j in range(m):
        dist = max(graph[i][j], dist)

# print(graph)
print(dist - 1)