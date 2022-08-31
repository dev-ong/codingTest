import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minAns = int(1e9)
start = []
link = []


def dfs(index):
    global minAns

    if index == n // 2:
        startSum = 0
        linkSum = 0
        for i in range(n):
            if i not in start:
                link.append(i)
        for i in range(n // 2 - 1):
            for j in range(i + 1, n // 2):
                startSum += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                linkSum += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        sol = abs(linkSum - startSum)
        if minAns > sol:
            minAns = sol
        link.clear()
        return

    for i in range(n):
        if i in start: continue
        if len(start) > 0 and start[len(start) - 1] > i: continue
        start.append(i)
        dfs(index + 1)
        start.pop()

dfs(0)
print(minAns)