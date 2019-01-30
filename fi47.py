a=[]
x=int(input())
for i in range(0,x):
      y=int(input())
      a.append(y)
a.sort()
print(a[0],a[len(a)-1])
