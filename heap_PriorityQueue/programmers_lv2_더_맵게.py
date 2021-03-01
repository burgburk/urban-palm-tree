import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    
    # Heap에 음식을 차례대로 삽입
    for food in scoville:
        heapq.heappush(heap, food)
    
    # 전부 K보다 맵게 & 섞을 음식 2개는 있어야 함
    while (heap[0] < K) and (len(heap)>=2):
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first+second*2)
        # print(heap)
        answer+=1
        
    # 끝까지 섞어서 1개 남았는데 K미만인 경우 -1을 return
    if heap[0] < K: return -1
    
    return answer
