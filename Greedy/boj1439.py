list=list(input())
cnt=0
for i in range(len(list)-1):
    if list[i] != list[i+1]:
        cnt=cnt+1
print((cnt+1)//2)