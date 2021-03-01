#### [문제](https://www.acmicpc.net/problem/9205)



#### 접근 및 풀이

* **`BFS/DFS`**로 출발지(=집)에서 목적지(=축제)까지 도착할 수 있는지 확인
* 각 탐색 시 **거리가 1000(맥주 20병*50m) 이내인 정점(=편의점)으로 제한**

* 정점을 좌표로 표현 **(visited 배열에 `T/F`가 아닌 방문한 편의점의 좌표를 저장하여 not in visited로 확인)**

#### 



#### Python3 코드

1. visited 배열에 `T/F`가 아닌 방문한 편의점의 좌표를 저장하여 not in visited로 확인

```python3
import sys
from collections import deque

t = int(input())

arr = []

for i in range(t):
    n = int(input())
    nodes = []
    
    for j in range(n+2):
        x, y = map(int, input().split())
        nodes.append([x, y])
    
    home, dest = nodes[0], nodes[n+1]
    
    stack, visited = [], []
    stack.append(home)
    visited.append(home)
    arrived = False
    
    # BFS의 경우 queue/deque사용
    while stack:
    
    	# queue/stack에서 꺼내서 방문
        current_x, current_y = stack.pop()
        
        # 방문한 노드(=편의점)이 축제현장인 경우 도착을 확인하고 종료
        if current_x == dest[0] and current_y == dest[1]:
            arrived = True
            break
            
        # 방문하지 않은 노드 중 1000m(=맥주 조건) 이내의 노드를 queue/stack에 추가
        for node in nodes:
            if node not in visited:
                dist = abs(current_x-node[0]) + abs(current_y-node[1])
                if dist <= 1000:
                    stack.append(node)
                    visited.append(node)
                    
    # Search 종료 후 성공 여부에 따라 출력
    if arrived:
        print("happy")
    else:
        print("sad")
```