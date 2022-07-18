import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]

visited = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            arr[y1 + j][x1 + i] = 1

# print(arr)

sol = 0
tmp = 0
cnt = []

def find(r, c):
    global tmp
    if r < 0 or r >= m or c < 0 or c >= n or arr[r][c] == 1:
        return False
    if visited[r][c] == 0:
        visited[r][c] = 1
        tmp += 1
        find(r + 1, c)
        find(r, c + 1)
        find(r - 1, c)
        find(r, c - 1)
        return True
    return False

for i in range(m):
    for j in range(n):
        if find(i, j) == True:
            sol += 1
            cnt.append(tmp)
            tmp = 0

print(sol)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i], end=' ')
