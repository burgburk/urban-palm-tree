def solution(new_id):
    temp = ""

    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            temp+=c
            
    temp = temp.lower()
    
    while ".." in temp:
        temp = temp.replace("..", ".")
        
    temp = temp.strip(".")
    
    l = len(temp)
    if l == 0:
        temp = "a"
    elif l >= 16:
        temp = temp[:15].rstrip(".")
        
    while len(temp) <= 2:
        temp += temp[-1]

    return temp
