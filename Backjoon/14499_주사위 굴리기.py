n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

def goDice(r, c, command):
    global x, y
    dr = [1, -1, 0, 0] # 하상우좌 4312
    dc = [0, 0, 1, -1]

    if command == 1:
        nr = r + dr[2]
        nc = c + dc[2]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return
        dice[2], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[2], dice[3]
    elif command == 2:
        nr = r + dr[3]
        nc = c + dc[3]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif command == 3:
        nr = r + dr[1]
        nc = c + dc[1]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
    else:
        nr = r + dr[0]
        nc = c + dc[0]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]

    if arr[nr][nc] == 0:
        arr[nr][nc] = dice[5]
    else:
        dice[5] = arr[nr][nc]
        arr[nr][nc] = 0
    x, y = nr, nc
    print(dice[2])

for command in commands:
    goDice(x, y, command)
