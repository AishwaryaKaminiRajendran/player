n=int(input())
a=[int(n) for n in input().split()]
f=0
b=[]
s=[]
for i in range(0,len(a)):
    f=f+a[i]
    b.append(f)
s=b[::-1]
for j in range(0,len(s)):
    print(s[j],end=" ")
