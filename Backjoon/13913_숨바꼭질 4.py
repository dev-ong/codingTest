from collections import deque

n, k = map(int, input().split())

M = 100001

visited = [0] * M
path = [0] * M
visited[n] = 1

# route = []

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            route = []
            while x != n:
                route.append(x)
                x = path[x]
            route.append(x)
            route.reverse()
            print(' '.join(map(str, route)))
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < M and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
                path[i] = x


bfs()
