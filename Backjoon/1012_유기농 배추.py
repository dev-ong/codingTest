import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())

    arr = [[0] * n for _ in range(m)]


    sol = 0

    for _ in range(k):
        r, c = map(int, input().split())
        arr[r][c] = 1

    def find(r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            return False

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        if arr[r][c] == 1:
            arr[r][c] = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                find(nr, nc)
            return True
        return False


    for i in range(m):
        for j in range(n):
            if find(i, j):
                sol += 1

    print(sol)
