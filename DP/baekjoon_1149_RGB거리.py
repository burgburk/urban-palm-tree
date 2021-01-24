# Using Memoization

n = int(input())

# Initialize result Array
res = [[0,0,0] for i in range(n)]
res[0] = list(map(int, input().split()))

for i in range(1, n):
    line = list(map(int, input().split()))
    res[i][0] = min(res[i-1][1], res[i-1][2]) + line[0]
    res[i][1] = min(res[i-1][0], res[i-1][2]) + line[1]
    res[i][2] = min(res[i-1][0], res[i-1][1]) + line[2]
    
print(min(res[n-1]))
