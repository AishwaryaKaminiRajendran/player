n=int(input())
a=[]
for i in range(2,n):
    if n%i==0:
        a.append(i)
for j in a:
    for k in range(2,j):
        if j%k==0:
            break
    else:
        print(j,end=" ")
