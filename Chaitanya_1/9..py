def amstrong(a):
      sum=0
      tem=a
      while tem>0:
            n= tem%10
            sum=sum+(n*n*n)
            tem=tem//10
      if sum==a:
            print("this is amstrong number:")
      else:
            print("this is not a amstrong number:")
      return sum
x=int(input("enter a any number:"))
amstrong(x)
            
                  
