m,l=map(int,input().split())
n,k=map(int,input().split())
p,r=map(int,input().split())
if(m==n and n==p) or (l==k and k==r):
    print("yes")
else:
    print("no")
