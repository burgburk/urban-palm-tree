### BFS 최단거리

```python3
from collections import defaultdict
from queue import Queue
```

### 1. Input 받기. 양방향 그래프임에 유의
```python3
N = int(input())
[m, n] = list(map(int, input().split()))
k = int(input())

g = defaultdict(list)

for i in range(k):
    [x, y] = list(map(int,input().split()))
    g[x].append(y)
    g[y].append(x)
```

### 2. 거리를 저장할 Depth 배열 초기화 & BFS를 수행할 Queue 초기화 후 m을 출발점으로 BFS 시작
```python3
depth = [-1]*(N+1)
visited = [False]*(N+1)
que = []
que.append(m)
depth[m] = 0
visited[m] = True

while que:
    start = que.pop(0)
    adj_nodes = g[start]
    for node in adj_nodes:
        
        # 아직 방문하지 않은 노드이면 queue에 삽입하고
        # depth 배열에 출발점으로부터 현재까지의 거리를 저장
        if (not visited[node]):
            que.append(node)

            # m으로부터의 거리가 출발한 노드보다 1 만큼 멂
            depth[node] = depth[start]+1
            visited[node] = True
print(depth[n])
```