n=input()
for i in range(0,len(n)):
    if n[i].isupper():
        print(n[i].lower(),end="")
    else:
        print(n[i].upper(),end="")
