import heapq

INF = int(1e9)

n, m = map(int, input().split())

s = int(input())

graph = [[] for _ in range(n + 1)]

dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(s):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)

for i in range(1, n + 1):
    if dis[i] == INF:
        print("INFINITY")
    else:
        print(dis[i])

