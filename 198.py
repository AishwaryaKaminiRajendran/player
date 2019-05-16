n=int(input())
a=[int(n) for n in input().split()]
b=min(a)
c=a.index(b)
d=max(a)
e=a.index(d)
print(abs(e-c))
