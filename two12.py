x=int(input())
s=0
c=x
while x!=0:
   r=x%10
   s=s*10+r
   x=x//10
print(s)
if c==s:
   print("yes")
else:
   print("no")
