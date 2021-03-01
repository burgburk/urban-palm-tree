# Undirected Graph에서 Connected Components 찾기
# DFS / BFS 수행 횟수 = Connected Component의 갯수

def solution(n, computers):
    answer = 0
    visited = [False]*n
    stack = []
    
    # Start DFS from each node(computer), if available
    for i in range(n):
        if visited[i]==False:
            stack.append(i)

            # Start DFS(방문할 노드가 스택에 남아있는 경우)
            # DFS를 Recursive하게 짜도 풀 수 있을 듯
            while stack: # len(stack) 으로 비어있는지 확인하는 것보다 훨씬 빠름
                start = stack.pop()
                visited[start] = True
                adj_coms = computers[start]
                for j in range(n):
                    if start != j:
                        if adj_coms[j]==1:
                            if not visited[j]:
                                stack.append(j)
                                
            # DFS가 끝나면 = 하나의 Connected Component의 모든 Node에 대한 Search가 완료된 것 = 한 네트워크의 모든 컴퓨터를 다 방문한 것 => 네트워크 갯수 +1
            answer+=1
    return answer
