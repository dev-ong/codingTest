import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))


def bfs(r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
    return arr[n-1][m-1]

print(bfs(0, 0))
