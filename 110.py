n=int(input())
a=[int(n) for n in input().split()]
f=0
q=[]
for i in range(0,len(a)):
    f=f+a[i]
    q.append(f)
f=0
b=[]
s=[]
for i in range(0,len(a)):
    f=f+a[i]
    b.append(f)
s=b[::-1]
for z in range(0,len(q)):
    for x in range(0,len(s)):
        if z==x:
            g=q[z]+s[x]
            print(g,end=" ")
