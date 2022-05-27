n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

sol = 0

for i in range(n):
    sol += A[i] * B[i]

print(sol)