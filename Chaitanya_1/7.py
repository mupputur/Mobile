def factors(a):
      count=1
      for i in range(1,a+1):
            count=count*i
      print(count)
x=int(input("enter a factors of a number:"))
factors(x)
