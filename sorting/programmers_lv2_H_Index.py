# 내림차순 정렬 후, counter보다 인용된 횟수가 적어지는 논문을 탐색하는 순간 종료

def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        if i >= citations[i]:
            return i
            
    # TC 9, 모든 반복문을 통과한 경우
    return n
