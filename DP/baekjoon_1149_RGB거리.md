[문제 링크](https://www.acmicpc.net/problem/1149)
2D Array 를 이용하여 각 stage별로 이전 stage에 저장된 값을 활용하여 계산\
**`Tabulation`**

```python3
n = int(input())

# Initialize an 2D Array

res = [[0,0,0] for i in range(n)]
res[0] = list(map(int, input().split()))

for i in range(1, n):
    line = list(map(int, input().split()))
    res[i][0] = min(res[i-1][1], res[i-1][2]) + line[0]
    res[i][1] = min(res[i-1][0], res[i-1][2]) + line[1]
    res[i][2] = min(res[i-1][0], res[i-1][1]) + line[2]
    
print(min(res[n-1]))
```
