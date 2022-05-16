n = int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
d = sorted(b)

sum=0
for i in range(n):
    k = a[i]*d[i]
    sum+=k
print(sum)