n=int(input())
length=list(map(int,input().split()))
price=list(map(int,input().split()))

result=0
m=price[0]
for i in range(n-1):
    if price[i]<m:
        m=price[i]
    result=result+m*length[i]
print(result)