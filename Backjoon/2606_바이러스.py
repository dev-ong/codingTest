n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n + 1)

sol = 0

def dfs(v):
    global sol
    visited[v] = 1

    for i in arr[v]:
        if visited[i] == 0:
            visited[i] = 1
            sol += 1
            dfs(i)

dfs(1)

print(sol)
