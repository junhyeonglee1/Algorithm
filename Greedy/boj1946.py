import sys

n=int(input())
for i in range(n):
    k=int(input())
    list=[]
    hire=1
    for j in range(k):
        a,b=map(int,sys.stdin.readline().split())
        list.append([a,b])

    list.sort()
    rank=list[0][1]

    for h in range(1,k):
        if list[h][1] < rank:
            rank=list[h][1]
            hire=hire+1
    print(hire)
    print(list)