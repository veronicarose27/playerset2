m=input()
l=list(m)
p=len(m)
k=[]
o=(p)//3
if(p<=3):
    k.append(l[0])
else:
    for i in range(0,o+1):
        k.append(l[i*3])
print("".join(k))
