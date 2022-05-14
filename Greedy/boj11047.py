n, k = map(int, input().split())
A=[]
for i in range(n):
    l = int(input())
    A.append(l)
count=0
money=k
A.sort(reverse=True)

for i in range(n):
    if money < A[i]:
        continue
    else:
        count += money // A[i]
        money = money % A[i]

print(count)