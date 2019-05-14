a,b=map(int,input().split())
f=1
while a>0:
    f=f*a
    a=a-1
x=1
while b>0:
    x=x*b
    b=b-1
s=f//x
print(s)
