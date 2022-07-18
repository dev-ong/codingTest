import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

queue = deque([])

def find(r, c):
    dis = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[r][c] = 1
    cnt = 0

    queue.append([r, c])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                dis[nr][nc] = dis[r][c] + 1
                visited[nr][nc] = 1
                cnt = max(cnt, dis[nr][nc])
                queue.append([nr, nc])
    return cnt

ans =0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            ans = max(ans, find(i, j))

print(ans)



