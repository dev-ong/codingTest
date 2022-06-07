n = 3
k = 5

arr = []

for i in range(1, n+1):
    arr.append(i)

perm_list = []

def perm(perm_list, idx):
    # perm_list = []
    if idx == n:
        print(arr)
        perm_list.append(arr)
    else:
        for i in range(idx, n):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(perm_list, idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]


perm(perm_list, 0)

print(perm_list)
# def solution(n, k):
#
#
#     answer = []
#     return answer
#
# print(solution(n, k))