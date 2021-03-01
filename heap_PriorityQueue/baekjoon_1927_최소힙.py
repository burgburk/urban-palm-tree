import heapq, sys
n = int(input())
arr = []
res = []
for i in range(n):
    num = int(sys.stdin.readline()) # input으로 받으면 시간 초과 ;;;
    if num == 0:
        if len(arr)==0:
            res.append(0)
        else:
            res.append(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)
for i in res:
    print(i)
