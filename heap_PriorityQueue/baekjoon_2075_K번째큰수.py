import heapq
import sys

n = int(input())
heap = []

# 첫 줄은 그대로 heap에 삽입
line = list(map(int, sys.stdin.readline().rstrip().split()))
for num in line:
    heapq.heappush(heap, num)
    
# 이후 (N-1)줄을 heap size = N으로 고정하며 pop하고 push | 고정 안하면 메모리 초과 ㅠㅠ
# 다음 line이 무조건 전 line 보다 크기때문에 pop하고 push해도 됨
for i in range(n-1):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for num in line:
        heapq.heappushpop(heap, num)
print(heap[0])
