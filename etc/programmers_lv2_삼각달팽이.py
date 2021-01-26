def solution(n):
    
    # Initialize
    res = []
    ans = []
    for i in range(n):
        res.append([0]*(i+1))

    # 시작 좌표, 채울 숫자
    x, y = 0, 0
    num = 1
    
    # i는 n부터 1씩 감소
    for i in range(n, 0, -1):
        
        # 아래로 i번
        if (n-i) % 3 == 0:
            for j in range(0, i):
                res[y][x] = num
                num+=1
                if j != i-1:
                    y+=1
                else: x+=1
        
        # 오른쪽으로 i번
        elif (n-i) % 3 == 1:
            for j in range(0, i):
                res[y][x] = num
                num+=1
                if j != i-1:
                    x+=1
                else:
                    x-=1
                    y-=1
                
        # 대각선으로 i번
        else:
            for j in range(0, i):
                res[y][x] = num
                num+=1
                if j != i-1:
                    x-=1
                    y-=1
                else:
                    y+=1
    
    # 답으로 변환
    for line in res:
        for i in line:
            ans.append(i)
            
    return ans
