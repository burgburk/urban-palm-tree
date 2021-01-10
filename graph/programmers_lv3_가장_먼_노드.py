# 깊이를 기록해가면서 BFS 수행하기

from queue import Queue

def solution(n, edges):
    g = [[] for i in range(n+1)]
    
    # Undirected Graph이므로 양방향으로 인접리스트를 추가해주어야 함에 유의
    for edge in edges:
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])
        
    # 편의를 위해,,, 정렬,,,
    for node in g:
        node.sort()
#     print(g)
    
    depth = [0]*(n+1)
    visited = [False]*(n+1)
    que = []
    que.append(1)
    depth[1] = 0
    visited[1] = True
    
    while que:
#         print("큐: ", que)
        start = que.pop(0)
#         print("Start Node:", start, end=' ')
        adj_nodes = g[start]
#         print("인접노드:",adj_nodes)
        for node in adj_nodes:
            # 아직 방문하지 않은 노드이면 queue에 삽입
            if (not visited[node]):
                que.append(node)
                # 출발 노드보다 거리 +1
                depth[node] = depth[start]+1
                visited[node] = True
                
    return depth.count(max(depth))
