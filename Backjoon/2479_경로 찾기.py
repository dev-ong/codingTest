n, k = map(int, input().split())
graph = [[] for _ in range(n)]

arr = [list(input()) for _ in range(n)]


for i in range(n - 1):
    cnt = 0
    for j in range(i + 1, n):
        for l in range(k):
            if arr[i][l] != arr[j][l]:
                if cnt > 1:
                    break
                cnt += 1

        if cnt == 1:
            graph[i].append(j)
            graph[j].append(i)

a, b = map(int, input().split())

print(graph)