from collections import deque

n, m = 5, 6
arr = [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1,], [1,1,1,1,1,1]]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))
    return arr[n-1][m-1]

print(bfs(0, 0))
