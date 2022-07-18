T = int(input())

def check(x):
    for i in range(x):
        if arr[i] == arr[x] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True

def find(x):
    global ans

    if x == n:
        ans += 1
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                find(x + 1)


for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * n
    ans = 0
    find(0)


    print('#{} {}'.format(tc, ans))