import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 0북 1동 2남 3서
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

visited[r][c] = 1

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turnLeft():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0

while True:
    turnLeft()
    nr = r + dr[d]
    nc = c + dc[d]

    if arr[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        cnt += 1
        r, c = nr, nc
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nr = r - dr[d]
        nc = c - dc[d]
        if arr[nr][nc] == 0:
            n, c = nr, nc
        else:
            break
        turn_time = 0

print(cnt)