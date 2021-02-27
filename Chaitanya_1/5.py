def prime_or_not(a):
      if a>1:
            count=0
            for i in range(1,a+1):
                  if a%i==0:
                        count=count+1
            if count==2:
                  print("this is  prime number:")
            else:
                  print("this  is nota prime number:")
            return count
a1=int(input("enter a number:"))
prime_or_not(a1)

"""
def prim(a):
      if (a%1==0) and  (a%a==0) and  (a%2 !=0):
            print("thie is even number:")
      else:
            print("not even:")
prim(7)"""
      
                  
