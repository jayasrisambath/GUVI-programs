a=[]
x=int(input())
for i in range(0,x):
     y=int(input())
     a.append(y)
a.sort()
l=len(a)
r=l//2
if r%2==0:
    print(a[r+1])
else:
    print(a[r])
