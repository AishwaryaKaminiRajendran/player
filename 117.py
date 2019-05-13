str1=input()
a=str1[::-1]
for i in range(0,len(a)):
    if i==len(a)-1:
        print(a[i])
    else:
        print(a[i],end="-")
