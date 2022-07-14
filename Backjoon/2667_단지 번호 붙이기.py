n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

visited = [[0] * (n+1) for _ in range(n+1)]

cnt_list = []
cnt = 0
sol = 0

def dfs(r, c):
    global cnt
    if r < 0 or c < 0 or r >= n or c >= n or arr[r][c] == 0:
        return False

    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
        dfs(r+1, c)
        dfs(r, c+1)
        dfs(r-1, c)
        dfs(r, c-1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt_list.append(cnt)
            sol += 1
            cnt = 0

cnt_list.sort()

print(sol)

for i in range(len(cnt_list)):
    print(cnt_list[i])