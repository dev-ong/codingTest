import sys
input = sys.stdin.readline

n = int(input())

arr = [0]

for i in range(n):
    arr.append(int(input()))

arr.append(0)

d = [0] * (n + 2)

d[1] = arr[1]
d[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    d[i] = max(d[i-3] + arr[i-1] + arr[i], d[i - 2] + arr[i], d[i - 1])
# print(arr)
print(max(d))