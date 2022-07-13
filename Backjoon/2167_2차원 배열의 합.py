import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())

    ans = 0

    for ii in range(x - i + 1):
        for jj in range(y - j + 1):
            ans += arr[i + ii - 1][j + jj - 1]

    print(ans)

