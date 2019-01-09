x=int(input())
y=x
s=0
while(x>0):
    r=x%10
    s=s+r*r*r
    x=x//10
if y==s:
   print("yes")
else:
   print("no")
