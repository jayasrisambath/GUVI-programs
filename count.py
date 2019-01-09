x=int(input())
c=0
if x>9 and x<-9:
      print("1")
else:
      while(x>0):
            r=x/10
            c=c+1
            x=r
      print(c)
