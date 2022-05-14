n = int(input())

list=[]

for i in range(n):
    x, y = map(int, input().split())
    list.append([x,y])

list= sorted(list, key = lambda x : (x[1],x[0]))
count = 1
endtime=list[0][1]
for i in range(1,n):
    if list[i][0]>=endtime:
        count+=1
        endtime=list[i][1]

print(count)