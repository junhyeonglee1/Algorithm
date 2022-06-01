n,m=map(int,input().split())
list1=[]
list2=[]
for i in range(m):
    a,b=map(int,input().split())
    list1.append(a)
    list2.append(b)

if min(list1)<= min(list2)*6:
    price=min(list1)*(n//6)+min(list2)*(n%6)
    if min(list1)<min(list2)*(n%6):
        price=min(list1)*(n//6+1)
else:
    price=min(list2)*n
print(price)