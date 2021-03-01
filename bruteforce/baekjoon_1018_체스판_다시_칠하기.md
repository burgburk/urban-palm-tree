[문제 링크](https://www.acmicpc.net/problem/1018)\

주어진 체스판을 8*8 단위로 쪼개서 2가지의 정답 체스판과 비교하며 색칠해아 하는 칸의 수를 count\

*2D Array를 다룰땐 x,y indexing을 주의할 것*


```python3
nm = input().split()
n, m = int(nm[0]), int(nm[1])
board = []

for i in range(n):
    board.append(list(input()))
    
res = []

target1 = list("WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW".split())
target2 = list("BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB BWBWBWBW WBWBWBWB".split())

for y in range(n-7):
    for x in range(m-7):
        count1= 0
        count2 = 0
        
        for i in range(0, 8):
            for j in range(0, 8):
                if board[y+i][x+j] != target1[i][j]:
                    count1+=1
        
        for i in range(0, 8):
            for j in range(0, 8):
                if board[y+i][x+j] != target2[i][j]:
                    count2+=1
                    
        res.append(min(count1, count2))
        
print(min(res))
```
