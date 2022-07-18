import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

s = int(input())

graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)

dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if dis[i] < min_value and not visited[i]:
            min_value = dis[i]
            index = i
    return index

def dijkstra(s):
    dis[s] = 0
    visited[s] = True
    for j in graph[s]:
        dis[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = dis[now] + j[1]
            if cost < dis[j[0]]:
                dis[j[0]] = cost

dijkstra(s)

for i in range(1, n + 1):
    if dis[i] == INF:
        print("INFINITY")
    else:
        print(dis[i])