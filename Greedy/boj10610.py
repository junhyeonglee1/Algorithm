list=list(input())

list.sort(reverse=True)
sum=0
for i in list:
    sum +=int(i)
if sum%3!=0 or '0'not in list:
    print(-1)
else:
    print(''.join(list))