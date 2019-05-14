a=int(input())
b=bin(a)
s=b[::-1]
for i in range(0,len(s)):
    if s[i]=="1":
        print(i+1)
        break
