n = int(input())

arr = [0] * n

def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True

def find(x):
    if x == n:
        for i in range(n):
            print(arr[i] + 1)
        exit()
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                find(x + 1)

find(0)