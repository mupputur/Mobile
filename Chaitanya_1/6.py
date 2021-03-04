def perfect_number(a):
      count=0
      for i in range(1,a):
            if a%i==0:
                  count=count+i
      if count==a:
            print("this is perfect number:")
      else:
            print("this is not perfect number:")
x = int(input("enter a number:"))
perfect_number(x)
                  
