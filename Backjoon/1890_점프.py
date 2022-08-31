n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]

d[0][0] = 1

for i in range(n):
    for j in range(n):
        if d[i][j] != 0 and arr[i][j] != 0:
            if j + arr[i][j] < n:
                d[i][j + arr[i][j]] += d[i][j]
            if i + arr[i][j] < n:
                d[i + arr[i][j]][j] += d[i][j]

print(d[n - 1][n - 1])