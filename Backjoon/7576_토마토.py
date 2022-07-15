from collections import deque

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

sol = 0

def bfs():
    while queue:
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                queue.append([nr, nc])

bfs()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    sol = max(sol, max(i))

print(sol - 1)