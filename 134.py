
n,i,r=map(int,input().split())
s=[int(n) for n in input().split()]
a=[]
for x in range(i-1,r):
    a.append(s[x])
print(min(a))
    
