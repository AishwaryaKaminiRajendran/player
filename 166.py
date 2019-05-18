import math
a,b= map(int,input().split())
f=1
while a>0:
    f=f*a
    a=a-1
#print(f)
g=1
while b>0:
    g=g*b
    b=b-1
#print(g)
if (f>g):
    r1=f
    r2=g
else:
    r1=g
    r2=f   
if(r1%r2==0):
    print (r2)
else:
    print(gcd(r2, r1%r2))



