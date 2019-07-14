p,q=map(int,input().split())
p1=list(map(int,input().split()))
q1=list(map(int,input().split()))
k=[]
y=[]
for i in range(0,q):
    k.append(q1[i])
    y.append(max(k))
print(*y)
