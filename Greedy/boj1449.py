n,l=map(int,input().split())
case = list(map(int,input().split()))
case.sort()
cnt=1
first=case[0]-0.5+l
for i in range(1,n):
    if first >= case[i]+0.5:
        continue
    else:
        first=case[i]-0.5+l
        cnt+=1
print(cnt)