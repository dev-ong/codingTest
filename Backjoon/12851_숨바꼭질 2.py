from collections import deque

n, k = map(int, input().split())
M = 100000
visited = [0] * (M + 1)

ans_cnt = 0
ans_way = 0

def bfs():
    global ans_cnt, ans_way
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        count = visited[x]

        if k == x:
            ans_cnt = count
            ans_way += 1
            continue

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < M + 1:
                if visited[i] == 0 or visited[i] == visited[x] + 1: # 방문 안했거나 하나 차이 나거나
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs()
print(ans_cnt)
print(ans_way)