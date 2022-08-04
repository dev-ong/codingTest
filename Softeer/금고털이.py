import sys

input = sys.stdin.readline

w, n = map(int, input().split())

sol = 0

arr = []

for _ in range(n):
    m, p = map(int, input().split())
    arr.append([p, m])

arr.sort(reverse=True)

i = 0

while w > 0:
    if arr[i][1] > 0:
        arr[i][1] -= 1
        w -= 1
        sol += arr[i][0]
    else:
        if (i + 1) < n:
            i += 1

print(sol)