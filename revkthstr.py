p,q=map(str,input().split())
q=int(q)
for i in range(q):
    p=p[-1]+p[:-1]
print(p)
