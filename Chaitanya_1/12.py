#Write a program construct two dimensional array and print the same.from array import *
def two_dimensional_array(a):
      c=[]
      for r in a:
            for c in r:
                  print(c,end = " ")
            print(c)
a1=[[2,3,4],[15, 6,10],[9,10,11],[12,15,8]]
two_dimensional_array(a1)
