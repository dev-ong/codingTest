import sys
input = sys.stdin.readline
import heapq

n = int(input())
left_heap, right_heap = [], []

for i in range(n):
    x = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)

    if len(left_heap) >= 1 and len(right_heap) >= 1 and left_heap[0] * -1 > right_heap[0]:
        max_num = heapq.heappop(left_heap) * -1
        min_num = heapq.heappop(right_heap)

        heapq.heappush(left_heap, min_num * -1)
        heapq.heappush(right_heap, max_num)

    print(left_heap[0] * -1)

