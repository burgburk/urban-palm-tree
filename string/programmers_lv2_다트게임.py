import re

def solution(dartResult):
  
    # 정규표현식으로 짤라먹기
    p = re.compile("(\d+)([a-zA-z])(\*|#)?")
    rounds = p.findall(dartResult)
    res = []
    
    for i, r in enumerate(rounds):
    
        # 라운드별 info 파싱
        score = int(r[0])
        bonus = r[1]
        option = r[2]

        # 지수 계산
        if bonus == "S":
            bonus = 1
        elif bonus == "D":
            bonus = 2
        elif bonus == "T":
            bonus = 3
            
        # 옵션 
        if option == '*':
            if i == 0:
                res.append(score**bonus*2)
            else:
                res[i-1]*=2
                res.append(score**bonus*2)
        elif option == "#":
            res.append(score**bonus*(-1))
        else:
            res.append(score**bonus)
            
    return sum(res)
