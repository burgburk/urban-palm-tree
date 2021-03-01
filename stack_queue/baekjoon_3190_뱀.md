#### [문제](https://www.acmicpc.net/problem/3190)



#### 접근

* **`시뮬레이션/Queue`**
* **`뱀을 Queue로 표현`**하고 board에서 움직이기
* 사과 = 2, 뱀 = 1, 빈 공간 = 0





#### 풀이

1. 매 초 현재 방향에 따라 머리를 먼저 움직이고 게임 종료 여부 확인
2. 사과가 있는지 확인 후 꼬리 자르기 `(Queue)`
3. 다음 초 진행





#### Python3 코드

##### input 받기 : board, queue, 방향 전환, 뱀 지정

```python3
from queue import deque

N = int(input())
board = [[0]*N for i in range(N)]
board[0][0] = 1

K = int(input())
for i in range(K):
    apple = list(map(int, input().split()))
    board[apple[0]-1][apple[1]-1] = 2

L = int(input())
dirs = {}
for i in range(L):
    change = input().split()
    dirs[int(change[0])] = change[1]

head_dir = 1
head = [0,0]
snake = deque()
snake.appendleft(head.copy())
```



##### 시뮬레이션 시작

```python3
t = 1
while t:

    # 현재 향하고 있는 방향에 따라 new head를 이동시킴
    if head_dir == 0:
        head[0] -= 1
    elif head_dir == 1:
        head[1] += 1
    elif head_dir == 2:
        head[0] += 1
    else:
        head[1] -= 1
        
    try:
        # 벽에 박는 경우
        if min(head[0], head[1]) < 0:
            raise Exception()
        
        # head가 몸에 닿은 경우 시간을 출력하고 종료
        if board[head[0]][head[1]] == 1:
            print(t)
            break
            
        # 벽이나 몸에 닿지 않았으면 일단 머리를 늘림
        # copy()를 이용해서 참조되는 head를 바꿔줌
        snake.appendleft(head.copy())    
           
        # 새 head의 위치에 사과가 없다면 꼬리를 자름(큐에서 pop하고 board에서 제거)
        if board[head[0]][head[1]] == 0:
            tail = snake.pop()
            board[tail[0]][tail[1]] = 0
        
        # 추가된 뱀 head를 board에 표시
        board[head[0]][head[1]] = 1
    
    # 벽에 닿은 경우
    except Exception as e:
        print(t)
        break
        
    # 행동이 끝난 후 다음 방향으로 전환
    try:
        if dirs[t] == "D":
            head_dir = (head_dir+1)%4
        else:
            head_dir = (head_dir-1)%4
    except Exception as e:
        pass
    
    t+=1
```



