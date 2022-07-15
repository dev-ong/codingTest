from collections import deque

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# print(arr)
# print(arr[0])
# print(arr[0][0][0])
dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
du = [0, 0, 0, 0, 1, -1]

queue = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i, j, k])

sol = 0

def find():
    while queue:
        u, r, c = queue.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nu = u + du[i]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nu < h and arr[nu][nr][nc] == 0:
                arr[nu][nr][nc] = arr[u][r][c] + 1
                queue.append([nu, nr, nc])

find()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            sol = max(sol, arr[i][j][k])

print(sol - 1)