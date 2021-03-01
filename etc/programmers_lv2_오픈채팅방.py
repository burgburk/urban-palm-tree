def solution(record):
    
    # Initialize
    answer = []
    users = {}
    
    # 각 Message를 type별로 처리
    for i, event in enumerate(record):
        message = ""
        event = event.split()
        t = event[0]
        
        # Enter일 경우 users에 등록
        if t == "Enter":
            message = "님이 들어왔습니다."
            users[event[1]] = event[2]
        
        # Leave일 경우
        elif t == "Leave":
            message = "님이 나갔습니다."
        
        # Change일 경우 닉네임 변경
        else:
            users[event[1]] = event[2]
            
        record[i] = [message, event[1]]
    
    # 최종 닉네임으로 메시지 출력
    for message in record:
        if message[0] != "":
            answer.append(users[message[1]]+message[0])
            
    return answer
