[문제 링크](https://www.acmicpc.net/problem/2231)

`eval(join)`보다 `sum(list)`가 더 빠르다\
전자는 시간 초과

```python3
n = int(input())

for i in range(n):
    if i + sum(list(map(int, str(i)))) == n:
        print(i)
        break
    if i == n-1:
        print(0)
```
