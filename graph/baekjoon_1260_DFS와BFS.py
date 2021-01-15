import sys
import heapq
from queue import Queue
[n, m, r] = list(map(int, input().split()))
g = {}

for i in range(n):
    g[i+1] = []
for i in range(m):
    [s, d] = list(map(int,input().split()))
    g[s].append(d)
    g[d].append(s)
for i in range(n):
    g[i+1].sort()
    
    
    
def dfs_iteration(graph, root):
    visited = [False] * (len(graph) + 1)
    stack = [root]
    res=""
    
    while stack:
        source = stack.pop()
        
        # 노드를 뽑을 때 체크!
        if not visited[source]:
            visited[source] = True
            res += " " + str(source)
            adj_nodes = graph[source]
            for node in adj_nodes[::-1]:
                # 방문 안 했으면 예약
                if not visited[node]:
                    stack.append(node)
    print(res[1:])



def bfs_iteration(graph, root):
    visited = [False] * (len(graph) + 1)
    queue = Queue()
    queue.put(root)
    res = ""
    
    while not queue.empty():
        source = queue.get()
        if not visited[source]:
            visited[source] = True
            res += " " + str(source)
            adj_nodes = graph[source]
            for node in adj_nodes:
                if not visited[node]:
                    queue.put(node)
    print(res[1:])
    
dfs_iteration(g, r)
bfs_iteration(g, r)
