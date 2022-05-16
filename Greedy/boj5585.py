n=1000 - int(input())
list=[500,100,50,10,5,1]
count=0
money=n
for i in list:
    if i>money:
        continue
    else:
        count = count + (money // i)
        money = money % i
print(count)