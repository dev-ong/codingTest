A, B, C = map(int, input().split())

def find(a, b):
    # b가 1이라면, a 나누기 C 리턴
    if b == 1:
        return a % C
    else:
        tmp = find(a, b // 2)
        if b % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C

print(find(A, B))
