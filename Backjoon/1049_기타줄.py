# n 끊어진 기타줄 m 기타줄 브랜드
n, m = map(int, input().split())
# 6개 패키지 가격, 낱개 가격
arr = []

for _ in range(m):
    price = map(int, input().split())
    arr.append(price)

six_list = sorted(arr, key=lambda x : x[0])
one_list = sorted(arr, key=lambda x : x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    sol = six_list[0][0] * (n // 6) + one_list[0][1] * (n % 6)
    if six_list[0][0] < one_list[0][1] * (n % 6):
        sol = six_list[0][0] * (n//6 + 1)
else:
    sol = one_list[0][1] * n

print(sol)


