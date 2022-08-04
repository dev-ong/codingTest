import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(m)]

visited = [[0] * n for _ in range(m)]

W_cnt = 0
B_cnt = 0

cnt = 0

def dfs(s, r, c):
    global cnt

    if 0 > r or r >= m or 0 > c or c >= n or arr[r][c] != s:
        return False

    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
        dfs(s, r + 1, c)
        dfs(s, r, c + 1)
        dfs(s, r - 1, c)
        dfs(s, r, c - 1)
        return True
    return False


for i in range(m):
    for j in range(n):
        if dfs('W', i, j):
            W_cnt += cnt ** 2
            cnt = 0
        elif dfs('B', i, j):
            B_cnt += cnt ** 2
            cnt = 0

print(W_cnt, B_cnt)