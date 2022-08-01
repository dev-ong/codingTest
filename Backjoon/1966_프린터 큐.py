for _ in range(int(input())):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'
    cnt = 0

    while prior:
        if prior[0] == max(prior):
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            else:
                prior.pop(0)
                index.pop(0)
        else:
            prior.append(prior.pop(0))
            index.append(index.pop(0))