n = int(input())
m = int(input())
couple=[[]*n for _ in range(n+1)]

for i in range(m):
    a, b= map(int,input().split())
    couple[a].append(b)
    couple[b].append(a)

visited=[False]*(n+1)
cnt=0

def dfs(x):
    global cnt
    visited[x] = True
    for i in couple[x]:
        if visited[i] == False:
            dfs(i)
            cnt +=1
dfs(1)

print(cnt)