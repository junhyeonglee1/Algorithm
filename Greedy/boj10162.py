n=int(input())

list=[500,60,10]
count=0

if n%10!=0:
    print(-1)
else:
    for i in list:

        if n<i:
             print(0,end=' ')
        else:
            count=n//i
            n=n%i
            print(count,end=' ')


