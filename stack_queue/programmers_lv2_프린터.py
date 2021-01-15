def solution(priorities, location):
    if len(priorities) == 1: return 1
    answer = 0
    ids = [0 for i in range(len(priorities))]
    ids[location] = 1

    while priorities:
        head, identifier = priorities.pop(0), ids.pop(0)
        print(head, identifier)
        if len(priorities) == 0: return answer+1
        if head < max(priorities):
            priorities.append(head)
            ids.append(identifier)
        else:
            answer+=1
            if identifier == 1:
                return answer
    return answer
