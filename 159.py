a,b=map(int,input().split())
c=a*b
d=bin(c)
c=0
for i in range(0,len(d)):
    if d[i]=="1":
        c=c+1
print(c)


        
        
