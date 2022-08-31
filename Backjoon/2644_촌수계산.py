from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)
visited[a] = 1

for _ in range(m):
    p, c = map(int, input().split())
    arr[p].append(c)
    arr[c].append(p)



def bfs(a):
    q = deque()
    q.append(a)

    while q:
        x = q.popleft()
        if x == b:
            print(visited[x] - 1)
            break
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
    else:
        print(-1)

bfs(a)


