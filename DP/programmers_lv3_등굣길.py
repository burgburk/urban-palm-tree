# 자신의 왼쪽 칸의 값(=해당 칸 까지의 최단 경로 수) + 자신의 윗쪽 칸의 값
# Memoization
# 10번 TC는 대체...

def solution(m, n, puddles):
    ways = [[0]*(m+1) for _ in range(n+1)]
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if x == 1 and y == 1:
                ways[x][y] = 1
                continue
            if [x,y] in puddles:
                ways[y][x] = 0
            else:
                ways[y][x] = ways[y-1][x] + ways[y][x-1] % 1000000007
    return ways[n][m]%1000000007
