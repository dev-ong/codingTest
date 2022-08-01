import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
M = 100001
visited = [0] * M
visited[n] = 1

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            break

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < M and visited[i] == 0:
                if i == x * 2:
                    visited[i] = visited[x] # 추가는 안해도 이동 횟수는 대입해줘야한다!
                    q.appendleft(i) # *2가 다른 연산자보다 우선순위를 가지도록 appendleft 해줘야함
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs()