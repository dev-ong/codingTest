import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

mh = 0

cnt = 0
cnt_list = []

for i in arr:
    for j in i:
        mh = max(mh, j)

def find(r, c, h):
    if r < 0 or c < 0 or r >= n or c >= n or arr[r][c] == 0:
        return False
    if visited[r][c] == 0 and arr[r][c] != 0:
        visited[r][c] = 1
        find(r + 1, c, h)
        find(r, c + 1, h)
        find(r - 1, c, h)
        find(r, c - 1, h)
        return True
    return False


for h in range(mh + 1):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= h:
                arr[i][j] = 0
    for i in range(n):
        for j in range(n):
            if find(i, j, h):
                cnt += 1
    cnt_list.append(cnt)
    cnt = 0


print(max(cnt_list))