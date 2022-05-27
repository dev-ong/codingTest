X = int(input())

arr = [1, 2, 4, 8, 16, 32, 64]

sol = 0

arr.sort(reverse=True)

for i in range(len(arr)):
    if X - arr[i] >= 0:
        X -= arr[i]
        sol += 1

print(sol)