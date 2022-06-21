T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    d = [0] * 31
    d[3] = 6
    d[4] = 7
    d[5] = 28


    for i in range(6, n + 1):
        # d[i] = (d[i - 1] + 2 * d[i - 2] + 5 * d[i - 3])
        d[i] = (d[i - 1] + 2 * d[i - 2] + 1 * d[i - 3])

    print('#{} {}'.format(tc, d[n]))