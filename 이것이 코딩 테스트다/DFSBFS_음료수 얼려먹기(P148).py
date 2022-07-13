arr = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

ans = 0


def dfs(r, c):
    if r <= -1 or r >= 4 or c <= -1 or c >= 5:
        return False

    if arr[r][c] == 0:
        arr[r][c] = 1

        dfs(r - 1, c)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r, c + 1)
        return True
    return False


for i in range(4):
    for j in range(5):
        if dfs(i, j) == True:
            ans += 1

print(ans)