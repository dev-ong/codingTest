import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

a, b = map(int, input().split())

m = b + 1

visited = [0] * m

def bfs():
    q = deque()
    q.append(a)

    while q:
        x = q.popleft()
        if x > b:
            continue

        if x == b:
            print(visited[x] + 1)
            break

        for i in (x * 2, int(str(x)+'1')):
            visited[i] = visited[x] + 1
            q.append(i)
    else:
        print(-1)

bfs()