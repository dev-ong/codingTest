n, r, c = map(int, input().split())

visit = 0

while n != 0:
    n -= 1
    size = 2 ** n

    # 1
    if r < size and c < size:
        visit += 0

    # 2
    elif r < size and c >= size:
        visit += size * size
        c -= size

    # 3
    elif r >= size and c < size:
        visit += size * size * 2
        r -= size

    # 4
    else:
        visit += size * size * 3
        r -= size
        c -= size

print(visit)