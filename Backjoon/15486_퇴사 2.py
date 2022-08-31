import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
d = [0] * (n + 1)

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

M = 0

for i in range(n):
    M = max(M, d[i])
    if i + t[i] > n:
        break
    d[i + t[i]] = max(M + p[i], d[i + t[i]])

print(max(d))

