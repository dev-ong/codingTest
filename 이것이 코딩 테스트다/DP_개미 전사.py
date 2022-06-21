# 4
# 1 3 1 5

n = int(input())
arr = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# DP 진행 (Bottom-Up)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n - 1])