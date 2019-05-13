a = int (input ())
s = 0 
b =[int (a) for a in input ().split ()]
for i in range (0,len(b)-1):
    j=i+1 
    s=s+b[i]+b[j]
print(s)    
