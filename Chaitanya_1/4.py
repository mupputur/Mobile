def fibonacci(x=0,y=1):
      for i in range(0,100):
            z=x+y
            if z>100:
                  break
            print(z)
            x = y
            y = z
fibonacci()
