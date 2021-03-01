from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    answer = sorted(numbers, key=cmp_to_key(isBigger), reverse=True) # Customized Comparator를 이용하여 정렬
    res = "".join(answer)
    if int(res) == 0: return "0"
    else: return res

# Customized Comparator. 두 숫자(A, B)를 이어붙였을때(AB vs BA) 더 큰 숫자가 되는 값을 크다고 정의함
def isBigger(a, b):
    x = int(a+b)
    y = int(b+a)
    if x > y: return 1
    elif x < y: return -1
    else: return 0
