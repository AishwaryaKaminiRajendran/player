s=input()
a=[]
b=[]
for i in range (0,len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
        a.append(s[i])
    else:
        b.append(s[i])
c=a+b
for j in range(0,len(c)):
    print(c[j],end="")
