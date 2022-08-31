import math

n = int(input())

trees = []

for _ in range(n):
    trees.append(int(input()))

between = []

for i in range(n - 1):
    between.append(trees[i + 1] - trees[i])

gap = between[0]

for j in range(1, n - 1):
    gap = math.gcd(gap, between[j])

sol = 0

for tree in between:
    sol += tree // gap - 1

print(sol)