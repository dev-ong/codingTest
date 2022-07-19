n, m = map(int, input().split())

INF = int(1e9)

arr = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            arr[a][b] = 0

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

distance = arr[1][k] + arr[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)