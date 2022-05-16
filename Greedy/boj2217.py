n=int(input())
list=[]
for i in range(n):
    k = int(input())
    list.append(k)
list.sort(reverse=True)

for i in range(n):
    list[i]=list[i]*(i+1)

print(max(list))
