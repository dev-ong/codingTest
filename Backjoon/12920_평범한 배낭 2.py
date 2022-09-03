N, M = map(int, input().split())

arr = []
d = [0 for _ in range(M + 1)]

for _ in range(N):
    W, C, K = map(int, input().split())

    # 비트 마스크 개념 도입
    i = 1
    while K > 0:
        m = min(i, K)
        arr.append((W * m, C * m))
        K -= i
        i *= 2

for W, C in arr:
    for i in range(M, W - 1, -1):
        d[i] = max(d[i], d[i - W] + C)

print(d[M])