#### [문제](https://www.acmicpc.net/problem/1167)



#### 접근

* **`DFS/BFS` 를 2번 수행**
* **`Undirected Graph(트리)` 내에서 `최장거리` 찾기**

* **`Tree이므로` Acyclic하고, 따라서 모든 경로가 유일 **
* V = 100000이고 Tree이므로  `Sparse Graph`. +메모리 제한 = 128M &rarr; 인접 리스트 사용(인접 배열 사용 시 메모리 초과)





#### 풀이

1. `DFS`/`BFS`로 임의의 한 정점(1번 정점)으로부터 다른 모든 정점까지의 거리를 구하고, 해당 노드로부터 `가장 먼 정점`을 찾음

2. 두 번째 ` DFS/BFS`로 1에서 구한 `가장 먼 정점`으로부터 다른 모든 정점까지의 거리를 각각 계산 후 가장 먼 거리(정점도 찾을 수 있음) 출력





#### Python3 코드

##### input 받기

```python3
import sys
from collections import defaultdict, deque

V = int(input())

# dictionary로 그래프 표현 ({source1: {dest1: distance, ...}})
g = defaultdict(dict) 

for i in range(V):
    line = list(map(int, input().split()))
    source = line[0]
    num_edges = int((len(line)-2)/2)
    for j in range(num_edges):
        g[source][line[2*j+1]] = line[2*j+2]
```



##### dfs 구현 (가정 먼 정점, 거리 return)

```python3
def dfs(u):
    
    # 방문 여부, 거리 초기화
    visited = [False]*(V+1)
    distance = [-1 for i in range(V+1)]
	
	# 사용할 stack/que 및 출발 정점의 거리, 방문 여부 초기화
    distance[u] = 0
    stack = []
    stack.append(u)
    visited[u] = True

	# search 진행
    while stack:
        source = stack.pop()
        adj_list = g[source]
        
        for dest in adj_list.keys():
            if not visited[dest]:
                visited[dest] = True
                # (지금까지 경로 + 타고 온 edge의 거리)를 거리 배열에 저장
                distance[dest] = distance[source]+adj_list[dest]
                stack.append(dest)
    
    # 가장 먼 정점 찾기
    max_distance = 0
    idx = 0
    for i in range(V+1):
        if distance[i] > max_distance:
            max_distance = distance[i]
            idx = i
    
    return idx, max_distance
```



##### DFS / BFS 2번 수행

```python3
node1, temp = dfs(1)
node2, res = dfs(node1)
print(res)
```

