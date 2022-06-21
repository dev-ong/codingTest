T = int(input())

d = [0] * 13
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(5, 11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for tc in range(1, T + 1):
    n = int(input())
    print(d[n])

