n=int(input())
a=[int(n) for n in input().split()]
for i in range(1,len(a)):
    j=i-1
    if a[i]%a[j]==0:
        print(a[i],end=" ")
