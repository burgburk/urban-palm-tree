n, m = int(input()),int(input())
g = {}
for i in range(n):
    g[i+1] = []

for i in range(m):
    line = list(map(int, input().split()))
    g[line[0]].append(line[1])
    g[line[1]].append(line[0])

# DFS
stack = [1]
visited = [False]*(n+1)
visited[1] = True
while stack:
    start = stack.pop(0)
    adj_coms = g[start]
    for com in adj_coms:
        if not visited[com]:
            stack.append(com)
            visited[com] = True

# Count Visited Nodes
print(visited.count(True)-1)
