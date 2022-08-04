import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

cnt = 0
cnt_list = []

def dfs(r, c):
    global cnt

    if r < 0 or c < 0 or r >= n or c >= m or arr[r][c] == 0:
        return False
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r - 1, c)
        dfs(r, c - 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt_list.append(cnt)
            cnt = 0

print(max(cnt_list))