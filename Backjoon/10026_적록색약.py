import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

arr = [list(input()) for _ in range(n)]

visited = [[0] * (n + 1) for _ in range(n + 1)]

sol_a = 0
sol_b = 0

def find(r, c, arr):
    global sol_a
    global sol_b
    visited[r][c] = 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[r][c] == arr[nr][nc]:
            find(nr, nc, arr)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            find(i, j, arr)
            sol_a += 1

# print(sol_a)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            find(i, j, arr)
            sol_b += 1

print(sol_a, sol_b)
