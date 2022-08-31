n, k = map(int, input().split())

arr = []

for _ in range(n):
    w, v = map(int, input().split())
    arr.append([w, v])

d = [0 for _ in range(k + 1)]

for item in arr:
    w, v = item
    # 최대 값 k부터 역순으로 들어갈 물건의 무게 w까지 순회
    for i in range(k, w - 1, -1):
        d[i] = max(d[i], d[i - w] + v)
    # 해당 위치의 최대 가치 d[i]와 들어갈 물건의 무게 w만큼 이전의
    # 최대 가치 d[j - w]에 물건의 가치 v를 더한 값 중에 최대 값
print(d[-1])