# RGB 거리

def solution(triangle):
    n = len(triangle)
    if n == 1: return triangle[0][0]
    answer = 0
    res = [triangle[0]]
    print(res)
    for i in range(1, len(triangle)):
        line = [0]*(i+1)
        for j in range(i+1):
            if j == 0:
                line[j] = res[i-1][j] + triangle[i][j]
            elif j == i:
                line[j] = res[i-1][j-1] + triangle[i][j]
            else:
                line[j] = max(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        res.append(line)
    return max(res[n-1])
